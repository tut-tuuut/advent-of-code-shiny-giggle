<?php

include('../utils.php');
include('input.php');


$blocks = explode("\t", $input);
$blocks = array_map('parseInt', $blocks);

function redistribute($array) {
    list($maxKey, $maxValue) = getMaxValueAndKey($array);
    $array[$maxKey] = 0;
    $size = count($array);
    for ($i = 1; $i <= $maxValue; $i++) {
        $array[($maxKey+$i)%$size] += 1;
    }
    return $array;
}

$metConfigurations = [];
$metConfigurations[implode(' ', $blocks)] = 'oh';
$steps = 0;
while (true) {
    $steps++;
    $blocks = redistribute($blocks);
    $blocksSignature = implode(' ', $blocks);
    if (isset($metConfigurations[$blocksSignature])) {
        break;
    } else {
        $metConfigurations[$blocksSignature] = 'ah';
    }
}

say($steps . ' is the result for part 1.');
say('configuration is: '.$blocksSignature);

$metConfigurations = [];
$metConfigurations[implode(' ', $blocks)] = 'oh';
$steps = 0;
while (true) {
    $steps++;
    $blocks = redistribute($blocks);
    $blocksSignature = implode(' ', $blocks);
    if (isset($metConfigurations[$blocksSignature])) {
        break;
    } else {
        $metConfigurations[$blocksSignature] = 'ah';
    }
}

say($steps . ' is the result for part 2.');
say('configuration is: '.$blocksSignature);

