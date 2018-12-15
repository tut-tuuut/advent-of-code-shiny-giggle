<?php

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');


$climate = new League\CLImate\CLImate;

$input = file_get_contents(__DIR__.'/input-2.txt');

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
$grid = makeTurn($grid);
draw($grid, $climate);

function makeTurn($grid) {
    $activeGrid = $grid;
    foreach ($grid as $y => $row) {
        foreach ($row as $x => $place) {
            if (!($place instanceof Unit)) {
                continue;
            }
            $place->move($activeGrid);
            $place->attack($activeGrid);
        }
    }
    return $activeGrid;
}

function draw($grid, $cli) {
    foreach ($grid as $row) {
        $str = implode('', $row);
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

    public function hit(Unit $unit)
    {
        $unit->takeDamage($this->attack);
    }

    public function takeDamage(int $damage)
    {
        $this->hp -= $damage;
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
            say('STOP');
            return false;
        }
        say($this->type.' let’s move!');
        list($targetX, $targetY) = $this->findWhereToMove($grid);
        $this->moveTo($targetX, $targetY, $grid);
    }

    private function moveTo($targetX, $targetY, &$grid)
    {
        say('I move to '.$targetX.'-'.$targetY);
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

    private function findWhereToMove(&$grid)
    {
        // for the moment, move randomly to a free neighbour,
        // we will see later for intelligence.
        // I just want to know if my unit can move.
        foreach ($this->findNeighbours($this->x, $this->y, $grid) as $neighbourInfo) {
            list($x, $y, $neighbour) = $neighbourInfo;
            if (is_string($neighbour) && $neighbour === '.') {
                return[$x, $y];
            }
        }
    }

    private function findNeighbours($x, $y, &$grid)
    {
        foreach ([
            [$this->y, $this->x - 1],
            [$this->y, $this->x + 1],
            [$this->y - 1, $this->x],
            [$this->y + 1, $this->x],
        ] as $neighbourCoordinates) {
            list($y, $x) = $neighbourCoordinates;
            if (isset($grid[$y][$x])) {
                yield [$x, $y, $grid[$y][$x]];
            }
        }
    }

    public function attack(&$grid)
    {
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