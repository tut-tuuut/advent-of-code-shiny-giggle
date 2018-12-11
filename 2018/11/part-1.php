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
checkEquals(cellPowerLevel(217, 196, 39),  0);
checkEquals(cellPowerLevel(101, 153, 71),  4);

// so, let's begin with the problem
// for each point in the grid, calculate the power level of its 3x3 square
const GRID_SIZE = 300;

say('calculating power levels…');
$powerLevels = [];
for ($i = 1; $i <= GRID_SIZE; $i++) {
    for ($j = 1; $j <= GRID_SIZE; $j++) {
        $powerLevels[$j][$i] = cellPowerLevel($i, $j);
    }
}

say('seeking for best power cell…');
$maxPower = 0;
$bestCoordinates = [];
for ($i = 1; $i <= GRID_SIZE - 2; $i++) {
    for ($j = 1; $j <= GRID_SIZE - 2; $j++) {
        $sum = 0;
        for ($x = $i; $x <= $i + 2; $x++) {
            for ($y = $j; $y <= $j + 2; $y++) {
                $sum += $powerLevels[$y][$x];
            }
        }
        if ($sum > $maxPower) {
            $maxPower = $sum;
            $bestCoordinates = [$i, $j];
        }
    }
}
say(bashColor(COLOR_NICE_BLUE, '[PART 1] ').implode(',', $bestCoordinates));