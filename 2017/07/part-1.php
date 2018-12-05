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
$individualWeights = [];
foreach ($progList as $line) {
    $matches = [];
    if (preg_match($regexParent, $line, $matches)) {
        // if regex matches, it is a parent program:
        // save it in the set
        $parentProgSet[$matches['name']] = "oh";
        // and save its individual weight for later…
        $individualWeights[$matches['name']] = (int)$matches['weight'];
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
unset($parentProgSet);

// part 2 : calculate the weight from the leaves
$newWeights = [];
foreach ($combinedWeights as $leaf => $weight) {
    $parent = $parentsByChild[$leaf];
    say($parent);
    if (isset($newWeights[$parent])) {
        continue;
    }
    $parentWeight = $individualWeights[$parent];
    $childrenWeights = [];
    foreach (findChildren($parent, $parentsByChild) as $child) {
        // here, maybe, deal with case in which one of the children
        // has no combinedWeight yet
        $childrenWeights[$child] = $combinedWeights[$child];
    }
    if (checkChildrenAreBalanced($childrenWeights)) {
        $parentWeight += array_sum($childrenWeights);
        $newWeights[$parent] = $parentWeight;
        say("$parent's weight: $parentWeight");
    } else {
        findSolutionForPart2($childrenWeights, $individualWeights);
        break;
    }
    say($childrenWeights);
}

function findChildren($parentName, $parentsNamesByChildren) {
    $children = [];
    foreach ($parentsNamesByChildren as $child => $parent) {
        if ($parent === $parentName) {
            $children[] = $child;
            if (count($children) === 7) {
                // no program in the list has more than 7 children
                return $children;
            }
        }
    }
    return $children;
}

function checkChildrenAreBalanced($children) {
    return (count(array_unique($children)) === 1);
}

function findSolutionForPart2($childrenCombinedWeights, $invididualWeights)
{
    // keep a trace of the "maybe correct" weight somewhere
    $correctWeight = $childrenCombinedWeights[key($childrenCombinedWeights)];
    // find which one is the unbalanced child
    while(!checkChildrenAreBalanced($childrenCombinedWeights)) {
        $child = key($childrenCombinedWeights);
        $weight = array_shift($childrenCombinedWeights);
    }
    if ($weight === $correctWeight) {
        $correctWeight = array_pop($childrenCombinedWeights);
    }
    say("$child is unbalanced, its total weight is $weight and we expected $correctWeight.");
    // find what its wheight should be
    $correctIndividualWeight = $invididualWeights[$child] + $correctWeight - $weight;
    say("it should weight $correctIndividualWeight instead.");
}
findSolutionForPart2(['titi' => 67, 'tata' => 68, 'tutu' => 67], ['tata' => 23]);
