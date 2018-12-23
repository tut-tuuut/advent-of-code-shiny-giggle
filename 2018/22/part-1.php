<?php

use League\CLImate\CLImate;
include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

const TARGET_X = 10; // 13;
const TARGET_Y = 10; //743;
const CAVE_DEPTH = 510; //8112;

const REGION_ROCK = 0;
const REGION_WET = 1;
const REGION_NARROW = 2;

const TOOL_CLIMB = 1;
const TOOL_TORCH = 2;
const TOOL_NONE = 3;


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
$beginning = [0, 0, TOOL_TORCH];
$target = [TARGET_X, TARGET_Y, TOOL_TORCH];

function calculateShortestPath($beginning, $target, &$grid)
{
    $cli->out('');
    // 7 minutes to change tools
    // 1 minute to move without changing tools
    $visited = [implode('-', $beginning)];
    $toCheck = [];
    foreach (findNeighbours($beginning, $grid) as $neighbourInfo) {
        list($x, $y, $neighbour) = $neighbourInfo;
        $visited[$x.'-'.$y] = true;
        if (!(is_string($neighbour) && $neighbour === '.')) {
            continue;
        }
        $toVisit[] = [
            'initial' => [$x, $y],
            'distance' => 1,
            'node' => [$x, $y],
        ];
    }
    while (count($toCheck)) {
        $cli->inline('.');
        $looking = array_pop($toCheck);
        $sortedNeighbours = [];
        foreach (findNeighbours($looking) as $neighbour) {
            $sortedNeighbours[timeFromAToB($toCheck, $neighbour).uniqid()] = $neighbour;
        }
        ksort($sortedNeighbours);
        foreach ($sortedNeighbours as $neighbour) {
            if (isset($visited[implode('-', $neighbour)])) {
                
            }
            $toCheck[] = $neighbour;
        }
    }
}

function findNeighbours($a, &$grid)
{
    list($xa, $ya, $toola) = $a;
    foreach ([-1, +1] as $offset) {
        foreach([TOOL_NONE, TOOL_CLIMB, TOOL_TORCH] as $tool) {
            if (isset($grid[$y][$xa + $offset])) {
                if (isToolValid($grid[$y][$xa + $offset], $tool)) {
                    yield [$xa + $offset, $y, $tool];
                }
            }
            if (isset( $grid[$y + $offset][$xa])) {
                if (isToolValid($grid[$y + $offset][$xa], $tool)) {
                    yield [$xa, $y + $offset, $tool];
                }
            }
        }
    }
}

function timeFromAToB($a, $b, &$grid)
{
    list($xa, $ya, $toola) = $a;
    list($xb, $yb, $toolb) = $b;
    // Check if $a and $b are valid: if not, return infinity
    if (!isToolValid($grid[$ya][$xa], $toola) || !isToolValid($grid[$yb][$xb], $toolb)) {
        return PHP_INT_MAX;
    }
    // Check if $a and $b are adjacent (normally OK, but who knows)
    if (abs($xa - $xb) + abs($ya - $yb) > 1) {
        return PHP_INT_MAX;
    }
    $time = abs($xa - $xb) + abs($ya - $yb); // 1 minute to move if cells are different
    // Check if you need to change tools
    if ($toola !== $toolb) {
        $time += 7;
    }
    return $time;
}

function isToolValid($cellType, $tool)
{
    if ($cellType === REGION_ROCK) {
        return ($tool === TOOL_TORCH || $tool === TOOL_CLIMB);
    } elseif ($cellType === REGION_WET) {
        return ($tool === TOOL_NONE || $tool === TOOL_CLIMB);
    } elseif ($cellType === REGION_NARROW) {
        return ($tool === TOOL_TORCH || $tool === TOOL_NONE);
    }
}

function getRiskLevel($x, $y, &$history)
{
    return getErosionLevel($x, $y, $history) % 3;
}

function getErosionLevel($x, $y, &$history)
{
    $index = getGeologicalIndex($x, $y, $history);
    return $index + CAVE_DEPTH % 20183;
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
        $result = $x * 16807;
    } elseif ($x === 0) {
        $result = $y * 48271;
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