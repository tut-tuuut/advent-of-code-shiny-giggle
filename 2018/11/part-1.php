<?php

include(__DIR__.'/../../utils.php');

const SN = 7803;

function hundredsDigit(int $a): int
{
    return (int)floor(($a%1000)/100);
}

function cellPowerLevel(int $x, int $y, int $sn = SN): int
{
    $rackId = $x + 10;
    $power = $rackId * $y;
    $power += $sn;
    $power = $power * $rackId;
    $power = hundredsDigit($power);
    return $power - 5;
}

// unit check of hundredsDigit
say('Check hundredsDigit: ', COLOR_NICE_PINK);
say(hundredsDigit(12055) . ' = 0');
say(hundredsDigit(12755) . ' = 7');
say(hundredsDigit(15) . ' = 0');
say(hundredsDigit(121) . ' = 1');

// unit check of cellPowerLevel
say('Check cellPowerLevel: ', COLOR_NICE_PINK);
say(cellPowerLevel(3, 5, 8). ' = 4');
say(cellPowerLevel(122, 79, 57). ' = -5');
say(cellPowerLevel(217, 169, 39). ' = 0'); // -3 ???
say(cellPowerLevel(101, 153, 71). ' = 4');
