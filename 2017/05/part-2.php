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
        if ($jump >= 3) {
            $input[$position] -= 1;
        } else {
            $input[$position] += 1;
        }
        $position += $jump;
        $numberOfSteps += 1;
        if ($numberOfSteps%10000000 === 0) {
            say("I’ve done $numberOfSteps steps, I’m not dead yet…");
        }
    }
}

say("I needed ".goFurther($intInput)." to get of this mess!");
