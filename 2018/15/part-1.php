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
draw($grid, $climate);
$grid = makeTurn($grid);

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
    $cli->clear();
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
        foreach (
            $this->findNeighbours($this->x, $this->y, $grid)
            as $neighbourInfo
        ) {
            $neighbour = $neighbourInfo[2];
            if ($neighbour instanceof Unit
            && $this->isEnemy($neighbour)) {
                say($this->type.' stop!');
                return false;
            }
        }
        say($this->type.' let’s move!');
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