<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// Parse input...
const INITIAL_STATE = '/initial state: ((?:#|\.)*)/';
const EVOLUTION = '/((?:#|\.)*) => (#|\.)/';
$evolutions = [];
$state = '';
foreach (explode(PHP_EOL, INPUT) as $inputRow) {
    $matches = [];
    if (preg_match(EVOLUTION, $inputRow, $matches)) {
        list(, $situation, $result) = $matches;
        $evolutions[$situation] = $result;
    } elseif (preg_match(INITIAL_STATE, $inputRow, $matches)) {
        $state = $matches[1];
    }
}

// Make situation evolute
say($state);
$pot = 0;
foreach (integers(20) as $number) {
    list($state, $pot) = spendTime($state, $pot, $evolutions);
}
say($state); say($pot);

// Check everything is ok
// say($state);
// var_dump($evolutions);

function spendTime($state, $numberOfFirstPot, $evolutions)
{
    $newNumberOfFirstPot = $numberOfFirstPot - 2;
    $newState = '';
    // deal with extreme left pots
    for ($i = 1; $i <= 4; $i++) {
        $pot = $i - 3;
        $situation = str_repeat('.', 5 - $i) . substr($state, 0, $i);
        $result = isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
        $newState .= $result;
    }
    // deal with pots we already know
    foreach (integers(strlen($state) - 2, 2) as $index) {
        $situation = substr($state, $index - 2, 5);
        $newState .= isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
    }
    // deal with extreme right pots
    for ($i = 1; $i <= 4; $i++) {
        $pot = strlen($state) - 2 + $i;
        $situation = substr($state, -$i, $i) . str_repeat('.', 5 - $i);
        $newState .= isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
       // say("last $i characters: $situation");
    }
    return [$newState, $newNumberOfFirstPot];
}