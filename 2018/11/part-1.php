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

function debug($coordinates, $array)
{
    list($topX, $topY, $size) = $coordinates;
    for ($i = $topX; $i < $topX + $size; $i++) {
        for ($j = $topY; $j < $topY + $size; $j++) {
            echo str_pad($array[$j][$i], 3) . ' ';
        }
        echo PHP_EOL;
    }
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

say('seeking for best power cell of size 3…', COLOR_NICE_PINK);
$maxPower = 0;
$bestCoordinates = [];
$powerOfSquares = [];
for ($i = 1; $i <= GRID_SIZE - 2; $i++) {
    for ($j = 1; $j <= GRID_SIZE - 2; $j++) {
        $sum = 0;
        for ($x = $i; $x <= $i + 2; $x++) {
            for ($y = $j; $y <= $j + 2; $y++) {
                $sum += $powerLevels[$y][$x];
            }
        }
        $powerOfSquares[$j][$i] = $sum;
        if ($sum > $maxPower) {
            $maxPower = $sum;
            $bestCoordinates = [$i, $j];
        }
    }
}
say(bashColor(COLOR_NICE_BLUE, '[PART 1] ').implode(',', $bestCoordinates));

say('seeking for best power square of any size…');
$bestCoordinates[] = 3;
// we already have calculated squares of size 3, let's continue with size 4
for ($squareSize = 4; $squareSize <= 300; $squareSize++) {
    $before = microtime(true);
    for ($i = 1; $i <= GRID_SIZE + 1 - $squareSize; $i++) {
        for ($j = 1; $j <= GRID_SIZE + 1 - $squareSize; $j++) {
            $sum = $powerOfSquares[$j][$i]; // this is the sum of the square of size $squareSize-1
            $initialSum = $sum;
            // visualized: I have X in $sum, I will add the sum of + to this sum
            // X x x + j
            // x x x + j+1
            // x x x + j+2
            // + + + + j+3
            // i  i+2
            // Lets add the sum of the column on the right
            for ($y = $j; $y < $j + $squareSize; $y++) {
                $sum += $powerLevels[$y][$i + $squareSize - 1];
            }
            // and the sum of the bottom
            for ($x = $i; $x < $i + $squareSize - 1; $x++) {
                $sum += $powerLevels[$j + $squareSize - 1][$x];
            }
            $powerOfSquares[$j][$i] = $sum;
            if ($sum > $maxPower) {
                $maxPower = $sum;
                $bestCoordinates = [$i, $j, $squareSize];
                say(bashColor(COLOR_NICE_BLUE, implode(',', $bestCoordinates)).' is a good candidate with a power of '.$maxPower);
            }
        }
    }
    $after = microtime(true);
    say('DONE with squares of size '.bashColor(COLOR_NICE_BLUE, $squareSize));
}
say(bashColor(COLOR_NICE_BLUE, '[PART 2] ').implode(',',$bestCoordinates));