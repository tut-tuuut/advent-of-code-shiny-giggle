<?php

include('input.php');

$input = explode(PHP_EOL, $inputString);

$frequency = 0;

foreach ($input as $inputRow) {
    $sign = $inputRow[0];
    $value = (int)substr($inputRow, 1);
    if ($sign === '+') {
        $frequency += $value;
    } elseif ($sign === '-') {
        $frequency -= $value;
    } else {
        echo 'Uh ???'.PHP_EOL;
    }
}

echo "Resulting frequency: " . $frequency . PHP_EOL;