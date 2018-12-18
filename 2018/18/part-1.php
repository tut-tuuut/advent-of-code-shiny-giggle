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
foreach (integers(10) as $minute) {
    foreach ($grid as $y => $row) {
        foreach ($row as $x => $cell) {
            $newGrid[$y][$x] = getNewCellContent($x, $y, $grid);
        }
    }
    $grid = $newGrid;
    foreach ($grid as $row) {
        $cli->out(implode('', $row));
    }
    sleep(1);
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
        foreach (getEveryNeighbour($x, $y, $grid) as $neighbour) {
            $hasLumberNeighbour = false;
            $hasTreeNeighbour = false;
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
