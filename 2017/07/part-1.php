<?php

// Thoughts:
// For the first part, we can simply ignore "leaf" programs.
// We are looking for the root of the tree.

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

/*$input = 'pbga (66)
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
cntj (57)';*/

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

say('---- - number of elements in combined weights before: '.count($combinedWeights));
for ($i = 0; $i < 3 && is_array($combinedWeights); $i++) {
    $combinedWeights = calculateWeightFromTheLeaves(
        $combinedWeights,
        $parentsByChild,
        $individualWeights
    );
    say(str_pad($i, 4).' - number of elements in combined weights: '.count($combinedWeights));
}

// part 2 : calculate the weight from the leaves
function calculateWeightFromTheLeaves($combinedWeights, $parentsByChild, $individualWeights) {
    $newWeights = [];
    foreach ($combinedWeights as $leaf => $weight) {
        $parent = $parentsByChild[$leaf];
        if (isset($combinedWeights[$parent])) {
            continue;
        }
        $skipParent = false;
        //say("analyzing $parent's children…");
        $parentWeight = $individualWeights[$parent];
        $childrenWeights = [];
        foreach (findChildren($parent, $parentsByChild) as $child) {
            // here, maybe, deal with case in which one of the children
            // has no combinedWeight yet? ---> yes.
            if (!isset($combinedWeights[$child])) {
                $skipParent = true;
                //say("$child has no combined weight yet => skip $parent");
                continue;
            }
            $childrenWeights[$child] = $combinedWeights[$child];
            //say("     $child weights ".$combinedWeights[$child]);
        }
        if ($skipParent) {
            //say('not every child has its combined weight calculated: skipping '.$parent);
            continue;
        }
        if (checkChildrenAreBalanced($childrenWeights)) {
            $parentWeight += array_sum($childrenWeights);
            $combinedWeights[$parent] = $parentWeight;
            //say("$parent's children are balanced : ".implode(' ', $childrenWeights));
            // unset($combinedWeights[$child]); in case of memory/perf issues
        } else {
            findSolutionForPart2($childrenWeights, $individualWeights);
            return true;
        }
    }
    return $combinedWeights;
}

function findChildren($parentName, $parentsNamesByChildren) {
    $children = [];
    foreach ($parentsNamesByChildren as $child => $parent) {
        if ($parent === $parentName) {
            $children[] = $child;
        }
    }
    return $children;
}

function checkChildrenAreBalanced($children) {
    return (count(array_unique($children)) === 1);
}

function findSolutionForPart2($childrenCombinedWeights, $invididualWeights)
{
    $firstChild = key($childrenCombinedWeights);
    $firstWeight = array_shift($childrenCombinedWeights);
    if (checkChildrenAreBalanced($childrenCombinedWeights)) {
        $correctWeight = array_shift($childrenCombinedWeights);
        say("$firstChild is unbalanced, its total weight is $firstWeight and we expected $correctWeight.");
        say("it weights ".$invididualWeights[$child]." alone.");
        $correctIndividualWeight = $invididualWeights[$firstChild] + $correctWeight - $firstWeight;
        say("it should weight $correctIndividualWeight instead.");
        return;
    }
    // keep a trace of the "correct" weight somewhere
    $correctWeight = $firstWeight;
    $weight = $correctWeight;
    // find which one is the unbalanced child
    while ($weight == $correctWeight) {
        $child = key($childrenCombinedWeights);
        $weight = array_shift($childrenCombinedWeights);
    }
    say("$child is unbalanced, its total weight is $weight and we expected $correctWeight.");
    // find what its wheight should be
    $correctIndividualWeight = $invididualWeights[$child] + $correctWeight - $weight;
    say("it weights ".$invididualWeights[$child]." alone.");
    say("it should weight $correctIndividualWeight instead.");
}
//findSolutionForPart2(['titi' => 67, 'tata' => 67, 'tutu' => 69], ['tata' => 23, 'tutu' => 22, 'titi' => 34]);
