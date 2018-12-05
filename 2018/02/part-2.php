<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

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

function findCommonCharacters($string1, $string2) {
    $result = '';
    for ($i = strlen($string1)-1; $i >= 0; $i--) {
        if ($string1[$i] === $string2[$i]) {
            $result = $string1[$i] . $result;
        }
    }
    return $result;
}

$size = count($input);
foreach ($input as $k1 => $row1) {
    for ($k2 = $k1+1; $k2 < $size; $k2++) {
        $row2 = $input[$k2];
        if (differByOneCharacter($row1, $row2)) {
            say('id 1: '.$row1);
            say('id 2: '.$row2);
            say('the answer is: '.findCommonCharacters($row1, $row2));
        }
    }
}
