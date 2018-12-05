<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

$result = 0;

$size = strlen($input);
$halfSize = $size/2;

for ($i = $size - 1; $i >= 0; $i--) {
    if ($input[$i] === $input[($i + $halfSize)%$size]) {
        $result += (int)$input[$i];
    }
}

say('result is: '.$result);