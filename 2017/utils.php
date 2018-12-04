<?php

function say($string) {
    echo $string . PHP_EOL;
}

function getMaxValueAndKey($array) {
    $maxValue = max($array);
    $maxKey = array_search($maxValue, $array);
    return [$maxKey, $maxValue];
}

function parseInt($str) {
    return (int)$str;
}