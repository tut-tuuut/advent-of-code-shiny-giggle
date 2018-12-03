<?php

include('../utils.php');

$nb = 289326;

function findPeriod($nb) {
    $i = -1;
    $previousSquare = 0;
    $newSquare = 0;
    while (true) {
        $i += 2;
        $previousSquare = $newSquare;
        $newSquare = $i * $i;
        if ($nb > $previousSquare && $nb <= $newSquare) {
            say("Your number $nb is between squares $previousSquare and $newSquare.");
            say("The period is $i.");
            return $i;
        }
    }
}

function generatePeriodicDistances($period) {
    $result = [];
    for ($i = -1 * (floor($period/2) - 1); $i <= floor($period/2); $i++) {
        $result[] = abs($i);
    }
    return $result;
}

$period = findPeriod($nb);
$firstPartOfDistance = floor($period / 2);

say('first part of distance is: '. $firstPartOfDistance);

$distances = generatePeriodicDistances($period);

$offset = ($nb - 1 - ($period-2)**2) % ($period - 1);

$secondPartOfDistance = $distances[$offset];

say("second part of distance is: $secondPartOfDistance");

say("total distance is: ".($firstPartOfDistance + $secondPartOfDistance));