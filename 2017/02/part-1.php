<?php

include('../utils.php');
include('input.php');

function extractMinAndMax($values) {
    $min = (int)$values[0];
    $max = (int)$values[0];
    foreach ($values as $value) {
        $value = (int)$value;
        if ($value > $max) {
            $max = $value;
        } elseif ($value < $min) {
            $min = $value;
        }
    }
    return [$min, $max];
}

$rows = explode(PHP_EOL, $input);
$checksum = 0;

foreach ($rows as $rawRow) {
    $row = explode("\t", $rawRow);
    list($min, $max) = extractMinAndMax($row);
    $checksum += $max - $min;
}

say('Result is: '.$checksum);