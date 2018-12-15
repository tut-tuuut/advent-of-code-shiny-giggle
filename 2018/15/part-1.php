<?php

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');


$climate = new League\CLImate\CLImate;

$climate->out('This prints to the terminal.');

$climate->red('Whoa now this text is red.');
$climate->blue('Blue? Wow!');
$climate->lightGreen('It is not easy being (light) green.');

$input = file_get_contents(__DIR__.'/input.txt');

$input = str_replace('G', '<red>G</red>', $input);
$input = str_replace('E', '<green>E</green>', $input);

$climate->clear();

$climate->out($input);


abstract class Unit
{
    private $x;
    private $y;
    private $hp;
    private $attack;
    private $type;

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
}

class Elf extends Unit
{
    private $type = 'elf';
}

class Goblin extends Unit
{
    private $type = 'goblin';
}