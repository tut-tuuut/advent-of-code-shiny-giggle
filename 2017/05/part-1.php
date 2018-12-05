<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// ---------------------------------------------------

$intInput = array_map('parseInt', explode(PHP_EOL, $input));

// ---------------------------------------------------

//$intInput = [0, 3, 0, 1, -3]; // Example given in instructions

function goFurther($input) {
    $numberOfSteps = 0;
    $position = 0;
    while (true) {
        if (!isset($input[$position])) {
            return $numberOfSteps;
        }
        $jump = $input[$position];
        $input[$position] += 1;
        $position += $jump;
        $numberOfSteps += 1;
    }
}

say(goFurther($intInput));
