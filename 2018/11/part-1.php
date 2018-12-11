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
checkEquals(hundredsDigit(12055), 0, 'for input 12055');
checkEquals(hundredsDigit(12755), 7, 'for input 12755');
checkEquals(hundredsDigit(15), 0, 'for input 15');
checkEquals(hundredsDigit(121), 1, 'for input 121');

// unit check of cellPowerLevel
say('Check cellPowerLevel: ', COLOR_NICE_PINK);
checkEquals(cellPowerLevel(3, 5, 8),  4);
checkEquals(cellPowerLevel(122, 79, 57),  -5);
checkEquals(cellPowerLevel(217, 169, 39),  0);
checkEquals(cellPowerLevel(101, 153, 71),  4);
