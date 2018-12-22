<?php

use League\CLImate\CLImate;
include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

const TARGET_X = 10;//13;
const TARGET_Y = 10;//743;

const CAVE_DEPTH = 520; // 8112;

$cli = new CLImate();

$history = [];
$totalRiskLevel = 0;
for ($y = 0; $y <= TARGET_Y; $y++) {
    for ($x = 0; $x <= TARGET_X; $x++) {
        $risk = getRiskLevel($x, $y, $history);
        $cli->inline($risk.' ');
        $totalRiskLevel += $risk;
    }
    $cli->out('');
}
say('part 1:'. $totalRiskLevel);

function getRiskLevel($x, $y, &$history)
{
    return (getErosionLevel($x, $y, $history))%3;
}

function getErosionLevel($x, $y, &$history)
{
    $index = getGeologicalIndex($x, $y, $history);
    return ($index + CAVE_DEPTH) % 20183;
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
        $result = ($x%20183) * (16807%20183);
    } elseif ($x === 0) {
        $result = ($y%20183) * (48271%20183);
    } else {
        $result = getGeologicalIndex($x - 1, $y, $history) * getGeologicalIndex($x, $y - 1, $history);
    }
    $history[$x][$y] = $result % 20183;
    return $result;
    // The region at the coordinates of the target has a geologic index of 0.
    // If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
    // If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
    // Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
}