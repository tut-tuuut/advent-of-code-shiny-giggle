<?php

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');


$climate = new League\CLImate\CLImate;

$input = file_get_contents(__DIR__.'/input-2.txt');

$input = str_replace('G', '<red>G</red>', $input);
$input = str_replace('E', '<green>E</green>', $input);

$climate->clear();

$climate->out($input);

$grid = [];
foreach (explode(PHP_EOL, $input) as $y => $inputrow) {
    foreach (str_split($inputrow) as $x => $char) {
        if ($char === '#' || $char === '.') {
            $grid[$y][$x] = $char;
        } elseif ($char === 'G') {
            $grid[$y][$x] = new Goblin($x, $y);
        } elseif ($char === 'E') {
            $grid[$y][$x] = new Elf($x, $y);
        }
    }
}
draw($grid, $climate);

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

    public function construct($x, $y)
    {
        $this->x = $x;
        $this->y = $y;
        $this->hp = 300;
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
}

class Elf extends Unit
{
    protected $type = 'E';
}

class Goblin extends Unit
{
    protected $type = 'G';
}