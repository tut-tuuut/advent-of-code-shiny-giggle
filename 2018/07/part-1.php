<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

/*$input = 'Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.';*/

$extractLetters = '/Step (\w) must be finished before step (\w) can begin./';
$steps = [];
foreach (explode(PHP_EOL, $input) as $row) {
    $matches = [];
    preg_match($extractLetters, $row, $matches);
    list( , $before, $after) = $matches;
    if (!isset($steps[$before])) {
        $steps[$before] = new Step($before);
    }
    if (!isset($steps[$after])) {
        $steps[$after] = new Step($after);
    }
    $steps[$before]->mustBeCompletedBefore($steps[$after]);
}

foreach ($steps as $step) {
    $step->debug();
}

while (count($steps) > 0) {
    doNextStep($steps);
}

function doNextStep(&$steps) {
    $next = min(findReadySteps($steps));
    $steps[$next]->do();
    unset($steps[$next]);
    return true;
}

function findReadySteps(&$steps) {
    $ready = [];
    foreach ($steps as $step) {
        if ($step->isReady()) {
            $ready[] = $step->getLetter();
        }
    }
    return $ready;
}

class Step
{
    private static $sequence = '';

    private $letter = '';
    private $done = false;

    /**
     * @var Step[]
     */
    private $before = [];

    /**
     * @var Step[]
     */
    private $after = [];

    public function __construct($letter)
    {
        $this->letter = $letter;
    }

    public function dependsOn(Step $step)
    {
        $this->before[] = $step;
    }

    public function mustBeCompletedBefore(Step $step) {
        $this->after[] = $step;
        $step->dependsOn($this);
    }

    public function isReady()
    {
        if ($this->done) {
            return true;
        }
        foreach ($this->before as $step) {
            if (!$step->isDone()) {
                return false;
            }
        }
        return true;
    }

    public function do()
    {
        self::$sequence .= $this->letter;
        $this->done = true;
        say(self::$sequence);
    }

    public function isDone()
    {
        return $this->done;
    }

    public function getLetter()
    {
        return $this->letter;
    }

    public function debug()
    {
        $str = '(';
        $str .= implode(', ', array_map(function($e) { return $e->getLetter(); }, $this->before));
        $str .= ') -> ' . $this->letter . ' -> (';
        $str .= implode(', ', array_map(function($e) { return $e->getLetter(); }, $this->after));
        $str .= ')';
        say($str);
    }
}