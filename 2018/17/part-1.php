<?php

use League\CLImate\CLImate;

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

$inputFile = $argv[1];

if (!$inputFile || !is_file(__DIR__.'/'.$inputFile)) {
    say('Please provide a valid file name.');
    die;
}

const CLAY = '#';
const SAND = '.';
const SOURCE = '+';
const FREE_WATER = '|';
const RESTING_WATER = '~';

const LEFT = -1;
const RIGHT = 1;

// First, parse input ------------------------------------------------------------------------
const EXTRACT_COORDINATES = '/(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)/';
$maxX = 0;
$maxY = 0;
$minX = 99999999;
$minY = 99999999;
$clayPoints = [];
foreach(explode(PHP_EOL, file_get_contents(__DIR__.'/'.$inputFile)) as $inputRow) {
    $matches = [];
    if (!preg_match(EXTRACT_COORDINATES, $inputRow, $matches)) {
        continue;
    }
    list(, $constCoord, $constValue, $variableCoord, $variableMin, $variableMax) = $matches;
    $constValue = (int)$constValue;
    $variableMin = (int)$variableMin;
    $variableMax = (int)$variableMax;

    if ($constCoord === 'x') { // vertical rectangle
        if ($maxX < $constValue) {
            $maxX = $constValue;
        } elseif ($minX > $constValue) {
            $minX = $constValue;
        }
        if ($maxY < $variableMax) {
            $maxY = $variableMax;
        }
        if ($minY > $variableMin) {
            $minY = $variableMin;
        }
    } elseif ($constCoord === 'y') { // horizontal rectangle
        if ($maxY < $constValue) {
            $maxY = $constValue;
        } elseif ($minY > $constValue) {
            $minY = $constValue;
        }
        if ($maxX < $variableMax) {
            $maxX = $variableMax;
        }
        if ($minX > $variableMin) {
            $minX = $variableMin;
        }
    }
    for ($i = $variableMin; $i <= $variableMax; $i++) {
        $clayPoints[] = [
            $constCoord => $constValue,
            $variableCoord => $i,
        ];
    }
}

// Then, generate the map -------------------------------------------------------------------------
$grid = array_fill(0, $maxY + 1, array_fill($minX, $maxX - $minX + 1, SAND));
$grid[0][500] = SOURCE; // water source
foreach ($clayPoints as $p) {
    $grid[$p['y']][$p['x']] = CLAY;
}
//draw($grid);
// Make water flow --------------------------------------------------------------------------------
$sources = [[0,500]]; // from which water falls
while(count($sources)) {
    $newSources = [];
    foreach ($sources as $source) {
        $newSources = array_merge($newSources, waterFlows($source, $grid));
    }
    $sources = $newSources;
}
draw($grid);
// When we have no sources anymore, we can begin to count wet cells -------------------------------
$wetCells = 0;
foreach ($grid as $y => $row) {
    $wetCells += count(array_filter($row, 'isWet'));
}
say("$wetCells in the grid!");

// ------------------------------------------------------------------------------------------------
function isWet($cell)
{
    return $cell === FREE_WATER || $cell === RESTING_WATER;
}

function isCrossable($cell)
{
    return $cell === SAND || $cell == FREE_WATER;
}

function waterFlows($source, &$grid)
{
    list($sy, $sx) = $source;
    $newSources = [];
    $depth = 0;
    $drill = true;
    $newWetCells = [];
    while ($drill) {
        $depth += 1;
        if (!isset($grid[$sy + $depth])) {
            $drill = false;
            continue;
        }
        if ($grid[$sy + $depth][$sx] === SAND) {
            $grid[$sy + $depth][$sx] = FREE_WATER;
            $newWetCells[] = [$sy + $depth, $sx];
            $drill = true;
        } else {
            $drill = false;
        }
    }

    foreach(array_reverse($newWetCells) as $cell) {
        $restWaterCandidates = [];
        // check if it can be transformed in resting water: surrounded by two # and above # or ~
        list($sy, $sx) = $cell;
        $isClosedOnBothSides = true;
        foreach ([LEFT, RIGHT] as $direction) {
            $flowToDirection = true;
            $toDirection = 0;
            $isClosedOnThisSide = false;
            while ($flowToDirection) {
                $toDirection += 1;
                if (!isset($grid[$sy][$sx + $direction * $toDirection])) {
                    $flowToDirection = false;
                    continue;
                }
                if (isCrossable($grid[$sy][$sx + $direction * $toDirection])
                && !isCrossable(f($grid, $sy + 1, $sx + $direction * $toDirection))) {
                    // on a clay or resting water surface
                    //      ->   X
                    //       #####
                    $restWaterCandidates[] = [$sy, $sx + $direction * $toDirection];
                } elseif (!isCrossable($grid[$sy][$sx + $direction * $toDirection])) {
                    // bumping on the wall of a container
                    //   -> X#
                    //      #
                    $isClosedOnThisSide = true;
                    $flowToDirection = false;
                } elseif (isCrossable($grid[$sy][$sx + $direction * $toDirection]) // a
                && isCrossable(f($grid, $sy + 1, $sx + $direction * $toDirection)) // b
                && !isCrossable(f($grid, $sy + 1, $sx + $direction * ($toDirection - 1))) ) { // c
                    // no side wall for current container on this direction
                    // -> a
                    // ##cb
                    $restWaterCandidates[] = [$sy, $sx + $direction * $toDirection];
                    $flowToDirection = false;
                }
            }
            $isClosedOnBothSides = $isClosedOnBothSides && $isClosedOnThisSide;
        }
        if ($isClosedOnBothSides) {
            $grid[$sy][$sx] = RESTING_WATER;
            foreach ($restWaterCandidates as $yx) {
                list($y, $x) = $yx;
                $grid[$y][$x] = RESTING_WATER;
            }
        } else {
            foreach ($restWaterCandidates as $yx) {
                list($y, $x) = $yx;
                $grid[$y][$x] = FREE_WATER;
                $newSources[] = $yx;
            }
        }
    }
    return $newSources;
}

// Draw map for debug ---------------------------------------------------------------------------
function draw(&$grid, $clear = true)
{
    $cli = new CLImate();
    if ($clear) { $cli->clear(); } else { $cli->out(''); }
    $cli->out(key($grid[0])); // display first x coordinate
    foreach ($grid as $y => $row) {
        $str = implode($row);
        $str = str_replace('+', '<light_blue>+</light_blue>', $str);
        $str = str_replace('|', '<light_blue>|</light_blue>', $str);
        $str = str_replace('~', '<light_blue>~</light_blue>', $str);
        $cli->out($str);
    }
}

// find value of cell on row y and col x, without yielding a notice if its unset
function f(&$grid, $y, $x, $default = SAND) {
    return isset($grid[$y][$x]) ? $grid[$y][$x] : $default;
}
