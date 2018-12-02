<?php

include('../utils.php');
include('input.php');

$input = explode(PHP_EOL, $inputString);

function calculateCounts($string) {
    $counts = [];
    for ($i = strlen($string)-1; $i >= 0; $i--) {
        $letter = $string[$i];
        if (!isset($counts[$letter])) {
            $counts[$letter];
        }
        $counts[$letter] += 1;
    }
    return $counts;
}

$numberWith2Letters = 0;
$numberWith3Letters = 0;

foreach ($input as $row) {
    $counts = calculateCounts($row);
    if (in_array(2, $counts)) {
        $numberWith2Letters += 1;
    }
    if (in_array(3, $counts)) {
        $numberWith3Letters += 1;
    }
}

say('String with 2 of any letter: '. $numberWith2Letters);
say('String with 3 of any letter: '. $numberWith3Letters);
say('The answer is: '. ($numberWith2Letters * $numberWith3Letters));