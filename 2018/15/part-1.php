<?php

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

$inputs = [
    [
        'file' => 'input-2.txt',
        'turns' => 47,
        'remaining' => 590
    ],
    [
        'file' => 'input-3.txt',
        'turns' => 37,
        'remaining' => 982
    ],
    [
        'file' => 'input-4.txt',
        'turns' => 46,
        'remaining' => 859
    ],
    [
        'file' => 'input-5.txt',
        'turns' => 35,
        'remaining' => 793
    ],
    [
        'file' => 'input-7.txt',
        'turns' => 54,
        'remaining' => 536
    ],
    [
        'file' => 'input-6.txt',
        'turns' => 20,
        'remaining' => 937
    ],
];

$climate = new League\CLImate\CLImate;

$inputInfo = $inputs[5];

$input = file_get_contents(__DIR__.'/'.$inputInfo['file']);

$grid = [];
foreach (explode(PHP_EOL, $input) as $y => $inputrow) {
    foreach (str_split($inputrow) as $x => $char) {
        if ($char === '#' || $char === '.') {
            $grid[$y][$x] = $char;
        } elseif ($char === 'G') {
            say('new goblin at '.$x.'-'.$y);
            $grid[$y][$x] = new Goblin($x, $y);
        } elseif ($char === 'E') {
            say('new elf at '.$x.'-'.$y);
            $grid[$y][$x] = new Elf($x, $y);
        }
    }
}
$climate->clear();
draw($grid, $climate);
foreach (integers(100, 1) as $completedTurns) {
    list($grid, $isOver) = makeTurn($grid);
    //$climate->clear();
    //draw($grid, $climate);
    //sleep(1);
    if ($isOver !== false) {
        say('hps remaining: '.$isOver);
        say('turns completed: '.$completedTurns);
        checkEquals($inputInfo['turns'],$completedTurns, 'completed turns');
        checkEquals($inputInfo['remaining'],$isOver, 'hp remaining');
        die;
    }
}

function checkPopulation($grid) {
    $goblinsLeft = false;
    $goblinsHp = 0;
    $elvesLeft = false;
    $elvesHp = 0;
    foreach ($grid as $row) {
        foreach ($row as $cell) {
            if (!($cell instanceof Unit)) {
                continue;
            }
            if ($cell instanceof Goblin) {
                $goblinsLeft = true;
                $goblinsHp += $cell->getHp();
            }
            if ($cell instanceof Elf) {
                $elvesLeft = true;
                $elvesHp += $cell->getHp();
            }
            if ($elvesLeft && $goblinsLeft) {
                return false;
            }
        }
    }
    return max($goblinsHp, $elvesHp);
}

function makeTurn($grid) {
    $activeGrid = $grid;
    foreach ($grid as $y => $row) {
        foreach ($row as $x => $place) {
            if (!($place instanceof Unit)) {
                continue;
            }
            $place->move($activeGrid);
            $place->attack($activeGrid);
            $hps = checkPopulation($activeGrid);
            if ($hps !== false) {
                return [$activeGrid, $hps];
            }
        }
    }
    return [$activeGrid, false];
}

function draw($grid, $cli) {
    foreach ($grid as $row) {
        $str = implode('', $row);
        foreach ($row as $cell) {
            if (!($cell instanceof Unit)) {
                continue;
            }
            $str .= ' ' . $cell->sayStatus();
        }
        $str = str_replace('G', '<red>G</red>', $str);
        $str = str_replace('E', '<green>E</green>', $str);
        $str = str_replace('.', ' ', $str);
        $cli->out($str);
    }
}
abstract class Unit
{
    private $x;
    private $y;
    private $hp;
    private $attack;

    public function __construct($x, $y)
    {
        $this->x = $x;
        $this->y = $y;
        $this->hp = 200;
        $this->attack = 3;
    }

    public function sayStatus()
    {
        return $this->type.'('.$this->hp.')';
    }

    public function getHp()
    {
        return $this->hp;
    }

    public function hit(Unit $unit, &$grid)
    {
        $unit->takeDamage($this->attack, $grid);
    }

    public function takeDamage(int $damage, &$grid)
    {
        $this->hp -= $damage;
        if ($this->hp <= 0) {
            $this->dieSadly($grid);
        }
    }

    private function dieSadly(&$grid)
    {
        $grid[$this->y][$this->x] = '.';
    }

    public function __toString()
    {
        return $this->type;
    }

    public function isEnemy(Unit $unit)
    {
        return ($this->type !== $unit->getType());
    }

    public function getType()
    {
        return $this->type;
    }

    public function move(&$grid)
    {
        if ($this->isNearAnEnemy($this->x, $this->y, $grid)) {
            return false;
        }
        list($targetX, $targetY) = $this->findWhereToMove($grid);
        $this->moveTo($targetX, $targetY, $grid);
    }

    private function moveTo($targetX, $targetY, &$grid)
    {
        if (!isset($grid[$targetY][$targetX])) {
            return;
        } elseif ($grid[$targetY][$targetX] !== '.') {
            return;
        }
        $grid[$targetY][$targetX] = $this;
        $grid[$this->y][$this->x] = '.';
        $this->x = $targetX;
        $this->y = $targetY;
    }

    private function isNearAnEnemy($x, $y, &$grid)
    {
        foreach (
            $this->findNeighbours($x, $y, $grid)
            as $neighbourInfo
        ) {
            $neighbour = $neighbourInfo[2];
            if ($neighbour instanceof Unit
            && $this->isEnemy($neighbour)) {
                return true;
            }
        }
        return false;
    }

    private function findEnemyToHit($x, $y, &$grid)
    {
        $target = null;
        foreach (
            $this->findNeighbours($x, $y, $grid)
            as $neighbourInfo
        ) {
            $neighbour = $neighbourInfo[2];
            if ($neighbour instanceof Unit
            && $this->isEnemy($neighbour)) {
                if (is_null($target)) {
                    $target = $neighbour;
                } elseif ($target->getHp() > $neighbour->getHp()) {
                    $target = $neighbour;
                }
            }
        }
        return $target;
    }

    private function findWhereToMove(&$grid)
    {
        // let's breadth-first-search the ideal spot
        $visited = [$this->x.'-'.$this->y => true];
        $toVisit = [];
        $found = [
            'distance' => 999999,
            'candidates' => [],
        ];
        // Fill the initial queue
        foreach ($this->findNeighbours($this->x, $this->y, $grid) as $neighbourInfo) {
            list($x, $y, $neighbour) = $neighbourInfo;
            $visited[$x.'-'.$y] = true;
            if (!(is_string($neighbour) && $neighbour === '.')) {
                continue;
            }
            $toVisit[] = [
                'initial' => [$x, $y],
                'distance' => 1,
                'node' => [$x, $y],
            ];
        }
        while (count($toVisit) > 0) {
            $info = array_shift($toVisit);
            list($x, $y) = $info['node'];
            if ($info['distance'] > $found['distance']) {
                break;
            }
            if ($this->isNearAnEnemy($x, $y, $grid)) {
                $found['distance'] = $info['distance'];
                $found['candidates'][] = $info['initial'];
            }
            foreach ($this->findNeighbours($x, $y, $grid) as $neighbourInfo) {
                list($nx, $ny, $nneighbour) = $neighbourInfo;
                $signature = $nx.'-'.$ny;
                if (isset($visited[$signature])) {
                    continue;
                }
                $visited[$signature] = true;
                if (!(is_string($nneighbour) && $nneighbour === '.')) {
                    continue;
                }
                $toVisit[] = [
                    'initial' => $info['initial'],
                    'distance' => $info['distance'] + 1,
                    'node' => [$nx, $ny],
                ];
            }
        }
        $candidates = $found['candidates'];
        if (count($candidates) === 0) {
            return false;
        }
        usort($candidates, function($a, $b) {
            list($xa, $ya) = $a;
            list($xb, $yb) = $b;
            if ($ya != $yb) {
                return ($ya < $yb) ? -1 : +1;
            }
            if ($xa != $xb) {
                return ($xa < $xb) ? -1 : +1;
            }
            return 0;
        });
        return array_shift($candidates);
    }

    private function findNeighbours($x, $y, &$grid)
    {
        foreach ([
            [$y - 1, $x], // top
            [$y, $x - 1], // left
            [$y, $x + 1], // right
            [$y + 1, $x], // bottom
        ] as $neighbourCoordinates) {
            list($y, $x) = $neighbourCoordinates;
            if (isset($grid[$y][$x])) {
                yield [$x, $y, $grid[$y][$x]];
            }
        }
    }

    public function attack(&$grid)
    {
        $enemyToHit = $this->findEnemyToHit($this->x, $this->y, $grid);
        if (!$enemyToHit) {
            return;
        }
        $this->hit($enemyToHit, $grid);
    }
}

class Elf extends Unit
{
    protected $type = 'E';
}

class Goblin extends Unit
{
    protected $type = 'G';
}