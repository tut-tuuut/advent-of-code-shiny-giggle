<?php

function say($something) {
    if (is_array($something)) {
        say (implode(' ', $something));
        return;
    }
    echo $something . PHP_EOL;
}

function getMaxValueAndKey($array) {
    $maxValue = max($array);
    $maxKey = array_search($maxValue, $array);
    return [$maxKey, $maxValue];
}

function parseInt($str) {
    return (int)$str;
}

function extractMinAndMax($values) {
    $min = (int)$values[0];
    $max = (int)$values[0];
    foreach ($values as $value) {
        $value = (int)$value;
        if ($value > $max) {
            $max = $value;
        } elseif ($value < $min) {
            $min = $value;
        }
    }
    return [$min, $max];
}

function sortString($string) {
    $chars = str_split($string);
    sort($chars);
    return implode('', $chars);
}

function generateAlphabet()
{
    foreach (str_split('abcdefghijklmnopqrstuvwxyz') as $letter) {
        yield $letter;
    }
}
