<?php

include(__DIR__.'/../../utils.php');


// examples

//list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [10, 1618, 8317];
//list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [13, 7999, 146373];
//list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [17, 1104, 2764];
//list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [21, 6111, 54718];
//list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [30, 5807, 37305];

// question for part 1
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [429, 70901, null];
// question for part2
list($nbOfPlayers, $lastMarbleWOrth, $expectedHS) = [429, 7090100, null];
// aaaand… this is a segfault

$circle = new CircleOfMarbles();
list($turn, $marble) = $circle->addFirstTwoMarbles();

$playersScores = array_fill(0, $nbOfPlayers, 0);
while($turn < $lastMarbleWOrth) {
    list($turn, $marble, $score) = $circle->makeTurn($turn, $marble);
    $playersScores[$turn%$nbOfPlayers] += $score;
}
say(bashColor(COLOR_NICE_BLUE, '[PART 1] ').max($playersScores));
if(!is_null($expectedHS)) {
    say('expected was '.$expectedHS);
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
            //$newMarble->debug($newMarble->value);
            return [$turn, $newMarble, 0];
        } else {
            $score = $newMarble->value;
            Marble::$activeMarbleCount--; // no insertion of new marble
            $sevenCounterClockwise = $marble->before->before->before->before->before->before->before;
            $score += $sevenCounterClockwise->value;
            $marble = $sevenCounterClockwise->after;
            $sevenCounterClockwise->remove();
            unset($sevenCounterClockwise);
            //$marble->debug($marble->value);
            return [$turn, $marble, $score];
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
    public static $activeMarbleCount = 0;

    public function __construct()
    {
        $this->value = self::$marbleCount++;
        self::$activeMarbleCount++;
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

    public function remove()
    {
        $this->before->after = $this->after;
        $this->after->before = $this->before;
        self::$activeMarbleCount--;
    }

    public function debug($value = null)
    {
        $marble = $this;
        for ($i = 0; $i < self::$activeMarbleCount; $i++) {
            say($marble->value . ' ', ($marble->value === $value ? COLOR_NICE_PINK : null), false);
            $marble = $marble->after;
        }
        say(''); // to have a EOL
    }
}