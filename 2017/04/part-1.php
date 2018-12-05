<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

function isValidPassphrase($string) {
    $words = [];
    foreach (explode(' ', $string) as $word) {
        $word = strtolower($word);
        if (isset($words[$word])) {
            return false;
        } else {
            $words[$word] = 'AH!';
        }
    }
    return true;
}

$valids = 0;
foreach (explode(PHP_EOL, $input) as $passphrase) {
    if (isValidPassphrase($passphrase)) {
        $valids += 1;
    }
}
say("There are $valids valid passphrases.");
