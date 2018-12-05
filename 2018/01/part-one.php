<?php

// What is the resulting frequency?

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

$input = explode(PHP_EOL, $inputString);

$frequency = 0;

foreach ($input as $inputRow) {
    $sign = $inputRow[0];
    $value = (int)substr($inputRow, 1);
    if ($sign === '+') {
        $frequency += $value;
    } elseif ($sign === '-') {
        $frequency -= $value;
    } else {
        say('Uh???');
    }
}

say("Resulting frequency: " . $frequency);