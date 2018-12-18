<?php

use League\CLImate\CLImate;

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

$inputFile = $argv[1];
$cli = new CLImate();

if (!$inputFile || !is_file(__DIR__.'/'.$inputFile)) {
    $cli->red('Please provide a valid file name.');
    die;
}

const TREES = '|';
const OPEN = '.';
const LUMBER = '#';

// Parse input… --------------------------------------------------------------
$grid = [];
foreach(explode(PHP_EOL, file_get_contents(__DIR__.'/'.$inputFile)) as $inputRow) {
    $grid[] = str_split($inputRow);
}

// debug constructed grid
foreach ($grid as $row) {
    $cli->out(implode('', $row));
}

$newGrid = [];
$cli->out('Calculating the 10 first steps...');
$progress = $cli->progress()->total(9);
foreach (integers(10) as $minute) {
    foreach ($grid as $y => $row) {
        foreach ($row as $x => $cell) {
            $newGrid[$y][$x] = getNewCellContent($x, $y, $grid);
        }
    }
    $grid = $newGrid;
    /*
    $cli->clear();
    foreach ($grid as $row) {
        $cli->out(implode('', $row));
    }*/
    $progress->current($minute);
}
list($trees, $lumbers) = countTreesAndLumbers($grid);
say("$trees trees and $lumbers lumbers");
say('[PART 1] '.($trees*$lumbers), COLOR_NICE_BLUE);

// Part 2
$cli->out('Calculating the 500 next steps...');
$progress = $cli->progress()->total(500);
foreach (integers(500) as $minute) {
    foreach ($grid as $y => $row) {
        foreach ($row as $x => $cell) {
            $newGrid[$y][$x] = getNewCellContent($x, $y, $grid);
        }
    }
    $grid = $newGrid;
    $progress->current($minute);
}

// Now we are probably in the periodic part: let's find a period
$searchWindow = 800;
say("Looking for a period in the $searchWindow next steps...");
$min = 999999999;
$max = 0;
$period = false;
$progress = $cli->progress()->total($searchWindow);
foreach (integers($searchWindow) as $minute) {
    foreach ($grid as $y => $row) {
        foreach ($row as $x => $cell) {
            $newGrid[$y][$x] = getNewCellContent($x, $y, $grid);
        }
    }
    $grid = $newGrid;
    list($trees, $lumbers) = countTreesAndLumbers($grid);
    $product = $trees * $lumbers;
    $progress->current($minute);
    /*file_put_contents(
        __DIR__.'/values.csv',
        implode(';',[$minute+510, $trees, $lumbers, $trees*$lumbers]) . PHP_EOL,
        FILE_APPEND
    );*/ // this was useful to check my hypothesis before truly calculating the period
}

// Utils ----------------------------------------------------------------------
function getEveryNeighbour($x, $y, &$grid)
{
    for ($i = $y - 1; $i <= $y + 1; $i++) {
        for ($j = $x - 1; $j <= $x + 1; $j++) {
            if ($i === $y && $j === $x) {
                continue;
            }
            if (isset($grid[$i][$j])) {
                yield $grid[$i][$j];
            }
        }
    }
}

function getNewCellContent($x, $y, &$grid)
{
    $content = $grid[$y][$x];
    if ($content === OPEN) {
        // An open acre will become filled with trees if three or more adjacent acres contained trees.
        $treesNeighbours = 0;
        foreach (getEveryNeighbour($x, $y, $grid) as $neighbour) {
            if($neighbour === TREES) {
                $treesNeighbours++;
                if ($treesNeighbours >= 3) {
                    return TREES;
                }
            }
        }
        // Otherwise, nothing happens.
        return OPEN;
    } elseif ($content === TREES) {
        // An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards.
        $lumberNeighbours = 0;
        foreach (getEveryNeighbour($x, $y, $grid) as $neighbour) {
            if($neighbour === LUMBER) {
                $lumberNeighbours++;
                if ($lumberNeighbours >= 3) {
                    return LUMBER;
                }
            }
        }
        // Otherwise, nothing happens.
        return TREES;
    } elseif ($content === LUMBER) {
        // An acre containing a lumberyard will remain a lumberyard if it was adjacent to
        //    - at least one other lumberyard
        //    - and at least one acre containing trees.
        $hasLumberNeighbour = false;
        $hasTreeNeighbour = false;
        foreach (getEveryNeighbour($x, $y, $grid) as $neighbour) {
            if($neighbour === TREES) {
                $hasTreeNeighbour = true;
            } elseif ($neighbour === LUMBER) {
                $hasLumberNeighbour = true;
            }
            if ($hasLumberNeighbour && $hasTreeNeighbour) {
                return LUMBER;
            }
        }
        // Otherwise, it becomes open.
        return OPEN;
    }
}

function isLumber($value)
{
    return $value === LUMBER;
}

function isTree($value)
{
    return $value === TREES;
}

function countTreesAndLumbers(&$grid)
{
    $nbOfTrees = 0;
    $nbOfLumbers = 0;
    foreach ($grid as $row) {
        $nbOfTrees += count(array_filter($row, 'isTree'));
        $nbOfLumbers += count(array_filter($row, 'isLumber'));
    }
    return [$nbOfTrees, $nbOfLumbers];
}

function fancyRepresentationOfABigNumber($number)
{
    return (string)$number;
}