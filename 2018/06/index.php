<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

$grid = []; // indexed by grid, containing the index of the zone
$points = []; // indexed by the index of the zone, containing i and j coordinates 
$maxI = 0;
$maxJ = 0;
$minI = 99999;
$minJ = 99999;
$areaSizes = [];
// get grid boundaries and points indexes
foreach (explode(PHP_EOL, $input) as $index => $row) {
    $index = generateHexCode($index);
    $areaSizes[$index] = 0;
    list($i, $j) = array_map('parseInt', explode(', ', $row));
    $grid[$i][$j] = $index;
    $points[$index] = [$i, $j];
    if ($maxI < $i) {
        $maxI = $i;
    } elseif ($minI > $i) {
        $minI = $i;
    }
    if ($maxJ < $j) {
        $maxJ = $j;
    } elseif ($minJ > $j) {
        $minJ = $j;
    }
}

$im = imagecreate(($maxJ - $minJ)*3 + 3, ($maxI - $minI)*3 + 3);
$colors = [];
$colors[''] = imagecolorallocate($im, 255, 255, 255);
foreach (array_keys($areaSizes) as $index) {
    $colors[$index] = imagecolorallocate($im, rand(40,235), rand(40,235), rand(40,235));
}

// generate grid and image <3
for ($i = $minI - 1; $i <= $maxI + 1; $i++) {
    for ($j = $minJ - 1; $j <= $maxJ + 1; $j++) {
        if (!isset($grid[$i][$j])) {
            $grid[$i][$j] = findClosestPoint([$i, $j], $points);
        }
        $index = $grid[$i][$j];
        if ($index) {
            $areaSizes[$index] += 1;
            imagefilledrectangle($im, ($j - $minJ)*3, ($i - $minI)*3, ($j - $minJ)*3 + 2, ($i - $minI)*3 + 2, $colors[$index]);
        }
    }
}

// draw points on the image
$black = imagecolorallocate($im, 0, 0, 0);
foreach ($points as $point) {
    $i = $point[0];
    $j = $point[1];
    imagefilledrectangle($im, ($j - $minJ)*3, ($i - $minI)*3, ($j - $minJ)*3 + 2, ($i - $minI)*3 + 2, $black);
}

// remove infinite areas from the count: I suppose the areas which touch the borders are infinite
for ($i = $minI - 1; $i <= $maxI + 1; $i++) {
    $index = $grid[$i][$minJ];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
        say('unsetting area size of '.$index);
    }
    $index = $grid[$i][$maxJ];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
        say('unsetting area size of '.$index);
    }
}
for ($j = $minJ - 1; $j <= $maxJ + 1; $j++) {
    $index = $grid[$minI][$j];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
        say('unsetting area size of '.$index);
    }
    $index = $grid[$maxI][$j];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
        say('unsetting area size of '.$index);
    }
}

say('the largest area has a size of '.max($areaSizes));

// save image
imagepng($im, 'image.png');

//var_dump($areaSizes);

function generateHexCode($i) {
    return substr(md5($i), 0, 6);
}

function manhattanDistance($a, $b) {
    return abs($a[0] - $b[0]) + abs($a[1] - $b[1]);
}

function findClosestPoint($a, $points) {
    $shortestDistance = 999999;
    $closestPoint = '';
    foreach ($points as $index => $point) {
        $distance = manhattanDistance($a, $point);
        if ($distance === $shortestDistance) {
            $closestPoint = '';
        } elseif ($distance < $shortestDistance) {
            $closestPoint = $index;
            $shortestDistance = $distance;
        }
    }
    return $closestPoint;
}
