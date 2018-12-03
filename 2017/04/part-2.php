<?php

include('../utils.php');
include('input.php');

function isValidPassphrase($string) {
    $words = [];
    foreach (explode(' ', $string) as $word) {
        $word = sortString(strtolower($word));
        if (isset($words[$word])) {
            return false;
        } else {
            $words[$word] = 'AH!';
        }
    }
    return true;
}

function sortString($string) {
    $chars = str_split($string);
    sort($chars);
    return implode('', $chars);
}

$valids = 0;
foreach (explode(PHP_EOL, $input) as $passphrase) {
    if (isValidPassphrase($passphrase)) {
        $valids += 1;
    }
}
say("There are $valids valid passphrases.");
