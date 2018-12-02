<?php

// What is the first frequency that is reached twice?

include('../utils.php');
include('input.php');

$input = explode(PHP_EOL, $inputString);

$frequency = 0;
$reachedFrequencies = [];
$reachedFrequencies[$frequency] = 'OH!';

$numberOfLoops = 0;

while(true) {
    $numberOfLoops++;
    say('Beginning loop #'.$numberOfLoops.'…');
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
        if (isset($reachedFrequencies[$frequency])) {
            say("First frequency reached twice: " . $frequency);
            die;
        } else {
            $reachedFrequencies[$frequency] = 'AH!';
        }
    }
}