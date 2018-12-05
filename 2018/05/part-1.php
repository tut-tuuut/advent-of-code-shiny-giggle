<?php

include('../utils.php');
include('input.php');


function generateNeedle()
{
    $letter = 'a';
    $needle = [];
    for ($letter = 'a'; $letter != 'aa'; $letter++) {
        $low = $letter;
        $up = strtoupper($letter);
        $needle[] = $up.$low;
        $needle[] = $low.$up;
    }
    return $needle;
}

$find = generateNeedle();

say("length of input: ". strlen($input));
$previousChecksum = '';
$newChecksum = md5($input);
while($newChecksum != $previousChecksum) {
    $previousChecksum = $newChecksum;
    $input = str_replace($find, '', $input);
    $newChecksum = md5($input);
    say("length of input: ". strlen($input));
}

//str_replace($needle, $replace, $input);