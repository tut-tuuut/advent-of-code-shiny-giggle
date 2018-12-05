<?php

// Thoughts:
// For the first part, we can simply ignore "leaf" programs.
// We are looking for the root of the tree.

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// regex to get name, weight and children of programs
$regex = '/^(?<name>\w+) \((?<weight>\d+)\) -> (?<children>.+)/';

$progList = explode(PHP_EOL, $input);
$parentProgSet = [];

foreach ($progList as $line) {
    $matches = [];
    if (preg_match($regex, $line, $matches)) {
        // if regex matches, it is a parent program:
        // save it in the set
        $parentProgSet[$matches['name']] = "oh";
    }
}

// then, unset every program in the set which has a parent:
// the last one will be the root

foreach ($progList as $line) {
    $matches = [];
    if (preg_match($regex, $line, $matches)) {
        $children = explode(', ', $matches['children']);
        foreach ($children as $child) {
            unset($parentProgSet[$child]);
        }
    }
}
if (count($parentProgSet) > 1) {
    say('uh oh');
}
say('the root is: '.key($parentProgSet));
