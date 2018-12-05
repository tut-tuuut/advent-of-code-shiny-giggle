<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

$rows = explode(PHP_EOL, $input);
$checksum = 0;

foreach ($rows as $rawRow) {
    $row = explode("\t", $rawRow);
    list($min, $max) = extractMinAndMax($row);
    $checksum += $max - $min;
}

say('Result is: '.$checksum);