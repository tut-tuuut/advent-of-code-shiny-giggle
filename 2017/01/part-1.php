<?php

include('../utils.php');
include('input.php');

$result = 0;

for ($i = strlen($input) - 2; $i >= 0; $i--) {
    if ($input[$i] === $input[$i + 1]) {
        $result += (int)$input[$i];
    }
}

if ($input[0] === $input[strlen($input) - 1]) {
    $result += (int)$input[0];
}

say('result is: '.$result);