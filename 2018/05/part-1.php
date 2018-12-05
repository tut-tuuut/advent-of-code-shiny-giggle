<?php

include('../utils.php');
include('input.php');


function generatePairs()
{
    $letter = 'a';
    $needle = [];
    foreach(generateAlphabet() as $letter) {
        $low = strtolower($letter);
        $up = strtoupper($letter);
        $needle[] = $up.$low;
        $needle[] = $low.$up;
    }
    return $needle;
}

function generateAlphabet()
{
    for ($letter = 'a'; $letter != 'aa'; $letter++) {
        yield $letter;
    }
}

function fullReaction($polymer) {
    $count = 1;
    $pairs = generatePairs();
    do {
        $polymer = str_replace($pairs, '', $polymer, $count);
    } while ($count > 0);
    return strlen($polymer);
}

say("part 1 : ". fullReaction($input));

