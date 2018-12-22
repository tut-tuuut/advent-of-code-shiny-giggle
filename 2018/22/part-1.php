<?php

use League\CLImate\CLImate;
include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

const TARGET_X = 10;//13;
const TARGET_Y = 10;//743;

const CAVE_DEPTH = 510;//8112;

$cli = new CLImate();

$history = [];
$totalRiskLevel = 0;
for ($y = 0; $y <= TARGET_Y; $y++) {
    for ($x = 0; $x <= TARGET_X; $x++) {
        $risk = getRiskLevel($x, $y, $history);
        if ($x === 0 && $y === 0) {
            $cli->inline('M');
        } elseif ($x === TARGET_X && $y === TARGET_Y) {
            $cli->inline('T');
        } else {
            $cli->inline(draw($risk));
        }
        $totalRiskLevel += $risk;
    }
    $cli->out('');
}
say('part 1: '. $totalRiskLevel);

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
        $result = getGeologicalIndex($x - 1, $y, $history) * getGeologicalIndex($x, $y - 1, $history);
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
    if ($value == 0) {
        return '.';
    } elseif ($value == 1) {
        return '=';
    } elseif ($value == 2) {
        return '|';
    }
    return '#';
}