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

// Check everything is ok
// say($state);
// var_dump($evolutions);
