<?php

// Thoughts:
// For the first part, we can simply ignore "leaf" programs.
// We are looking for the root of the tree.

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

$input = 'pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)';

// regex to get name, weight and children of programs
$regexParent = '/^(?<name>\w+) \((?<weight>\d+)\) -> (?<children>.+)/';
// regex to get only name and weight of program
$regexChild = '/^(?<name>\w+) \((?<weight>\d+)\)/';

$progList = explode(PHP_EOL, $input);
$parentProgSet = []; // set of every program which is a parent (to find the root)
$parentsByChild = []; // used to store the parent of every child program
$combinedWeights = []; // weights of towers over the programs, indexed by name

foreach ($progList as $line) {
    $matches = [];
    if (preg_match($regexParent, $line, $matches)) {
        // if regex matches, it is a parent program:
        // save it in the set
        $parentProgSet[$matches['name']] = "oh";
    } else {
        // it's a leaf program, we are interested in its weight for later…
        preg_match($regexChild, $line, $matches);
        $combinedWeights[$matches['name']] = (int)$matches['weight'];
    }
}

foreach ($progList as $line) {
    $matches = [];
    if (preg_match($regexParent, $line, $matches)) {
        $parent = $matches['name'];
        $children = explode(', ', $matches['children']);
        foreach ($children as $child) {
            // (part 1) unset every program in the set which has a parent:
            // the last one will be the root.
            unset($parentProgSet[$child]);
            // (part 2) for each child, store who is its parent
            $parentsByChild[$child] = $parent;
        }
    }
}
if (count($parentProgSet) > 1) {
    say('uh oh');
}
say('[PART 1] the root is: '.key($parentProgSet));
