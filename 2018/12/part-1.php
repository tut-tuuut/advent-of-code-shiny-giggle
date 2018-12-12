<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// Parse input...
const INITIAL_STATE = '/initial state: ((?:#|\.)*)/';
const EVOLUTION = '/((?:#|\.)*) => (#|\.)/';
$evolutions = [];
$state = '';
foreach (explode(PHP_EOL, INPUT) as $inputRow) {
    $matches = [];
    if (preg_match(EVOLUTION, $inputRow, $matches)) {
        list(, $situation, $result) = $matches;
        $evolutions[$situation] = $result;
    } elseif (preg_match(INITIAL_STATE, $inputRow, $matches)) {
        $state = $matches[1];
    }
}

// Make situation evolute
say($state);

$pot = 0;
$img = imagecreatetruecolor(1300, 500);
$black = imagecolorallocate($img, 0, 0, 0);
$green = imageColorAllocate($img, 0, 240, 90);

drawState($img, $state, 0, 0, $green);

foreach (integers(20) as $idx => $number) {
    list($state, $pot) = spendTime($state, $pot, $evolutions);
    drawState($img, $state, $pot, $idx + 1, $green);
}
imagepng($img, 'evolution.png');

// Count number of pots with a plant inside
$sum = 0;
foreach(integers(strlen($state), $pot) as $strIdx => $potIdx) {
    if ($state[$strIdx] == '#') {
        $sum += $potIdx;
    }
}
say(bashColor(COLOR_NICE_BLUE, '[PART 1] ').$sum);

function spendTime($state, $numberOfFirstPot, $evolutions)
{
    $newNumberOfFirstPot = $numberOfFirstPot - 2;
    $newState = '';
    // deal with extreme left pots
    //say('left');
    for ($i = 1; $i <= 4; $i++) {
        $pot = $i - 3;
        $situation = str_repeat('.', 5 - $i) . substr($state, 0, $i);
        $result = isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
        //say($situation . ' -> '.$result);
        $newState .= $result;
    }
    // deal with pots we already know
    //say('middle');
    foreach (integers(strlen($state) - 4, 2) as $index) {
        $situation = substr($state, $index - 2, 5);
        $result = isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
        //say($situation . ' -> '.$result);
        $newState .= isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
    }
    // deal with extreme right pots
    //say('to the right');
    for ($i = 4; $i >= 1; $i--) {
        $pot = strlen($state) - 2 + $i;
        $situation = substr($state, -$i, $i) . str_repeat('.', 5 - $i);
        $result = isset($evolutions[$situation]) ? $evolutions[$situation] : '.';
        //say($situation.' -> '.$result);
        $newState .= $result;
    }
    return [$newState, $newNumberOfFirstPot];
}

function drawState($image, $state, $initialPot, $generation, $color)
{
    $white = imagecolorallocate($image, 100,120,100);
    foreach(integers(strlen($state), $initialPot) as $strIdx => $potIdx) {
        $cx = $potIdx * 5 + 30;
        $cy = 17 + $generation * 10;
        if ($potIdx%10 === 0) {
            imageline($image, $cx, 0, $cx, 1000, $white);
        }
        if ($generation%10 === 0) {
            imageline($image, 0, $cy, 1900, $cy, $white);
        }
        if ($state[$strIdx] !== '#') { continue; }

        imagefilledellipse($image, $cx, $cy, 4, 7, $color);
    }
}