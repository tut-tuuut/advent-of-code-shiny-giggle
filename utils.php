<?php

const COLOR_NICE_PINK = 197;
const COLOR_NICE_RED = 196;
const COLOR_NICE_BLUE = 69;
const COLOR_NICE_GREEN = 46;

function say($something, $color = null, $withEol = true) {
    if (is_array($something)) {
        $something = (implode(' ', $something));
    }
    if (!is_null($color) && is_int($color) && $color <= 256) {
        $something = bashColor($color, $something);
    }
    echo $something . ($withEol ? PHP_EOL : '');
}

function bashColor($color, $string) {
    return "\e[38;5;${color}m".$string."\e[39m";
}

function checkEquals($expected, $actual, $message = '')
{
    if (!$message) {
        $message = "$expected == $actual";
    }
    if ($expected == $actual) {
        say(bashColor(COLOR_NICE_GREEN, "[OK] ").$message);
    } else {
        say(bashColor(COLOR_NICE_RED, "[KO] ").$message);
    }
}

function getMaxValueAndKey($array) {
    $maxValue = max($array);
    $maxKey = array_search($maxValue, $array);
    return [$maxKey, $maxValue];
}

function parseInt($str) {
    return (int)$str;
}

function integers(int $number, $start = 0) {
    for ($i = 0 ; $i < $number ; $i++) {
        yield $i => $i + $start;
    }
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
