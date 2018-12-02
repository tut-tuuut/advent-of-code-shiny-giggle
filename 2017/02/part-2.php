<?php

include('../utils.php');
include('input.php');

function parseInt($value) {
    return (int)$value;
}

function lookForWhatTheUserNeeds($sortedValues) {
    $size = count($sortedValues);
    foreach ($sortedValues as $k => $biggerValue) {
        for ($i = $k+1; $i < $size; $i++) {
            $smallerValue = $sortedValues[$i];
            if ($biggerValue % $smallerValue === 0) {
                return $biggerValue / $smallerValue;
            }
        }
    }
    say('oh… we have a problem: '.implode(' ', $sortedValues));
}

$rows = explode(PHP_EOL, $input);
$result = 0;

foreach ($rows as $rawRow) {
    $row = array_map(parseInt, explode("\t", $rawRow));
    rsort($row);
    $result += lookForWhatTheUserNeeds($row);
}

say('The result is: '.$result);