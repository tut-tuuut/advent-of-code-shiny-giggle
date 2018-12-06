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
$im2 = imagecreate(($maxJ - $minJ)*3 + 3, ($maxI - $minI)*3 + 3);
$colors = [];
$colors[''] = imagecolorallocate($im, 255, 255, 255);
$black2 = imagecolorallocate($im2, 48,42,106);

// generate colors for both images
foreach (array_keys($areaSizes) as $index) {
    $colors[$index] = imagecolorallocate($im, rand(40,235), rand(40,235), rand(40,235));
}
$blue2 = imagecolorallocate($im2, 135,137,224);
$green2 = imagecolorallocate($im2, 206,220,255);

// generate grid and image <3
$goodArea = 0;
for ($i = $minI - 1; $i <= $maxI + 1; $i++) {
    for ($j = $minJ - 1; $j <= $maxJ + 1; $j++) {
        if (!isset($grid[$i][$j])) {
            $grid[$i][$j] = findClosestPoint([$i, $j], $points);
        }
        $totalDistance = getTotalDistance([$i, $j], $points);
        if ($totalDistance <= 10000) {
            $goodArea += 1;
            imagefilledrectangle($im2, ($j - $minJ)*3, ($i - $minI)*3, ($j - $minJ)*3 + 2, ($i - $minI)*3 + 2, $blue2);
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
    imagefilledrectangle($im2, ($j - $minJ)*3, ($i - $minI)*3, ($j - $minJ)*3 + 2, ($i - $minI)*3 + 2, $green2);
}

// remove infinite areas from the count: I suppose the areas which touch the borders are infinite
for ($i = $minI - 1; $i <= $maxI + 1; $i++) {
    $index = $grid[$i][$minJ];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
    }
    $index = $grid[$i][$maxJ];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
    }
}
for ($j = $minJ - 1; $j <= $maxJ + 1; $j++) {
    $index = $grid[$minI][$j];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
    }
    $index = $grid[$maxI][$j];
    if (isset($areaSizes[$index])) {
        unset($areaSizes[$index]);
    }
}

say('[PART 1] the largest area has a size of '.max($areaSizes));

// Calculating the barycenter
$iSum = $jSum = 0;
foreach ($points as $index => $point) {
    $iSum += $point[0];
    $jSum += $point[1];
}
$baryI = (int)$iSum/count($points);
$baryJ = (int)$jSum/count($points);
say("barycenter could be at: $baryI, $baryJ");
say(getTotalDistance([$baryI, $baryJ], $points));
imagerectangle($im, ($baryJ - $minJ)*3 - 2, ($baryI - $minI)*3 - 2, ($baryJ - $minJ)*3 + 4, ($baryI - $minI)*3 + 4, $black);
imagerectangle($im2, ($baryJ - $minJ)*3 - 2, ($baryI - $minI)*3 - 2, ($baryJ - $minJ)*3 + 4, ($baryI - $minI)*3 + 4, $green2);

$index = $grid[$baryI][$baryJ];
$size = $areaSizes[$index];

say('[PART 2] the result is '.$goodArea);
// save image
imagepng($im, 'image.png');
imagepng($im2, 'image2.png');


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

function getTotalDistance($a, $points) {
    $sum = 0;
    foreach ($points as $index => $point) {
        $sum += manhattanDistance($a, $point);
    }
    return $sum;
}
