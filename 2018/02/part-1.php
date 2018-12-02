<?php

// What is the resulting frequency?

include('../utils.php');
include('input.php');

$input = explode(PHP_EOL, $inputString);

function containsExactlyTwoOfAnyLetter($string) {
    $counts = [];
    for ($i = strlen($string)-1; $i >= 0; $i--) {
        $letter = $string[$i];
        if (!isset($counts[$letter])) {
            $counts[$letter];
        }
        $counts[$letter] += 1;
    }
    return in_array(2, $counts);
}

var_dump(containsExactlyTwoOfAnyLetter('abcdeafg'));