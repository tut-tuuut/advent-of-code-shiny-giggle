<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

$input = 'Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.';

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

class Step
{
    private $letter = '';

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
}