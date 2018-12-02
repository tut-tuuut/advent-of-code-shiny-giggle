<?php

include('../utils.php');
include('input.php');

$input = explode(PHP_EOL, $inputString);

function differByOneCharacter($string1, $string2) {
    $numberOfDifferences = 0;
    for ($i = strlen($string1)-1; $i >= 0; $i--) {
        if ($string1[$i] !== $string2[$i]) {
            $numberOfDifferences += 1;
        }
        if ($numberOfDifferences > 1) {
            return false;
        }
    }
    return $numberOfDifferences === 1;
}

$size = count($input);
foreach ($input as $k1 => $row1) {
    for ($k2 = $k1+1; $k2 < $size; $k2++) {
        $row2 = $input[$k2];
        if (differByOneCharacter($row1, $row2)) {
            say('id 1: '.$row1);
            say('id 2: '.$row2);
            say('keys: '.implode(' and ', [$k1, $k2]));
        }
    }
}
