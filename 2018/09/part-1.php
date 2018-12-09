<?php

include(__DIR__.'/../../utils.php');


// examples

list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [10, 1618, 8317];
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [13, 7999, 146373];
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [17, 1104, 2764];
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [21, 6111, 54718];
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [30, 5807, 37305];

// question for part 1
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [429, 70901, null];

$circle = new CircleOfMarbles();
list($turn, $marble) = $circle->addFirstTwoMarbles();

while($turn < 20) {
    list($turn, $marble) = $circle->makeTurn($turn, $marble);
}

class CircleOfMarbles
{
    public function addFirstTwoMarbles()
    {
        $firstMarble = new Marble();
        $secondMarble = new Marble();
        $firstMarble->after = $secondMarble;
        $secondMarble->after = $firstMarble;
        $firstMarble->before = $secondMarble;
        $secondMarble->before = $firstMarble;
        return [1, $secondMarble];
    }

    public function makeTurn($turn, $marble)
    {
        $turn++;
        $newMarble = new Marble();
        if ($newMarble->value%23 > 0) {
            $marble->after->insertAfter($newMarble);
            $marble->debug($newMarble->value);
            return [$turn, $newMarble];
        } else {

        }
        return ;
    }
}

class Marble
{
    public $value;
    public $before;
    public $after;
    public static $marbleCount = 0;

    public function __construct()
    {
        $this->value = self::$marbleCount++;
    }

    public function insertAfter(Marble $m)
    {
        // before:
        // $this ---> $after
        // after:
        // $this ---> $m ----> $after
        $m->after = $this->after;
        $this->after->before = $m;
        $m->before = $this;
        $this->after = $m;
    }

    public function debug($value = null)
    {
        $marble = $this;
        for ($i = 0; $i < self::$marbleCount; $i++) {
            say($marble->value . ' ', ($marble->value === $value ? COLOR_NICE_PINK : null), false);
            $marble = $marble->after;
        }
        say(''); // to have a EOL
    }
}