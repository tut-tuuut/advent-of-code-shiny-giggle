<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');


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

function fullReaction($polymer) {
    $count = 1;
    $pairs = generatePairs();
    do {
        $polymer = str_replace($pairs, '', $polymer, $count);
    } while ($count > 0);
    return strlen($polymer);
}

say("part 1 : ". fullReaction($input));

$bestLength = strlen($input);

foreach (generateAlphabet() as $letter) {
    $reducedInput = str_replace([strtolower($letter), strtoupper($letter)], '', $input);
    $reducedLength = fullReaction($reducedInput);
    if ($reducedLength < $bestLength) {
        $bestLength = $reducedLength;
        say ($letter . ' is a good candidate with a reduced length of '.$bestLength);
    }
}
say("part 2 $bestLength");