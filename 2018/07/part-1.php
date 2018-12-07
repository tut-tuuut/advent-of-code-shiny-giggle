<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');


$extractLetters = '/Step (\w) must be finished before step (\w) can begin./';
foreach (explode(PHP_EOL, $input) as $row) {
    $matches = [];
    preg_match($extractLetters, $row, $matches);
    list( , $before, $after) = $matches;
    say("$before -> $after");
}
