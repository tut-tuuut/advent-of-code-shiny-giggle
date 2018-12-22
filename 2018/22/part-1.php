<?php

use League\CLImate\CLImate;
include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

const TARGET_X = 13;
const TARGET_Y = 743;

const REGION_ROCK = 0;
const REGION_WET = 1;
const REGION_NARROW = 2;

const TOOL_CLIMB = 1;
const TOOL_TORCH = 2;
const TOOL_NONE = 3;

const CAVE_DEPTH = 8112;

$cli = new CLImate();

$history = [];
$totalRiskLevel = 0;
$progress = $cli->progress()->total(TARGET_Y);
$cli->out('Calculating risk level in area...');
for ($y = 0; $y <= TARGET_Y; $y++) {
    for ($x = 0; $x <= TARGET_X; $x++) {
        $totalRiskLevel += getRiskLevel($x, $y, $history);
    }
    $progress->current($y);
}
say('part 1: '. $totalRiskLevel);

$cli->out('Calculating map...');
$progress = $cli->progress()->total(TARGET_Y + 100);
$grid = [];
for ($y = 0; $y <= TARGET_Y + 100; $y++) {
    for ($x = 0; $x <= TARGET_X + 100; $x++) {
        $grid[$y][$x] = getRiskLevel($x, $y, $history);
    }
    $progress->current($y);
}
$cli->out('Done. Now, just calculating the shortest path...');

function getRiskLevel($x, $y, &$history)
{
    return gmp_mod(getErosionLevel($x, $y, $history), 3);
}

function getErosionLevel($x, $y, &$history)
{
    $index = getGeologicalIndex($x, $y, $history);
    return gmp_mod($index + CAVE_DEPTH, 20183);
}

function getGeologicalIndex($x, $y, &$history)
{
    if (isset($history[$x][$y])) {
        return $history[$x][$y];
    }
    // The region at 0,0 (the mouth of the cave) has a geologic index of 0.
    if ($x === 0 && $y === 0) {
        $result = 0;
    } elseif ($y === TARGET_Y && $x === TARGET_X) {
        $result = 0;
    } elseif ($y === 0) {
        $result = gmp_mul($x, 16807);
    } elseif ($x === 0) {
        $result = gmp_mul($y, 48271);
    } else {
        $result = getErosionLevel($x - 1, $y, $history) * getErosionLevel($x, $y - 1, $history);
    }
    $history[$x][$y] = $result;
    return $result;
    // The region at the coordinates of the target has a geologic index of 0.
    // If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
    // If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
    // Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
}

function draw($value)
{
    if ($value == REGION_ROCK) {
        return '.';
    } elseif ($value == REGION_WET) {
        return '=';
    } elseif ($value == REGION_NARROW) {
        return '|';
    }
    return '#';
}