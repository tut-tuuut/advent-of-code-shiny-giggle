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

// Then, generate the map -----------------------------------------------------------------------
$grid = array_fill(0, $maxY + 1, array_fill($minX, $maxX - $minX + 1, SAND));
$grid[0][500] = SOURCE; // water source
foreach ($clayPoints as $p) {
    $grid[$p['y']][$p['x']] = CLAY;
}

// Draw map for debug ---------------------------------------------------------------------------
foreach ($grid as $y => $row) {
    //say(implode($row));
}
