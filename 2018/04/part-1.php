<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// --- extract and sort input
$data = explode(PHP_EOL, $input);
sort($data);

// ---- regex to extract date and text
$regexForDate = '/\[1518-(\d{2})-(\d{2}) (\d{2})\:(\d{2})\] (.+)/';
// ---- regex to see if this is a "falls asleep" or "wakes up"
$regexForGuardId = '/Guard #(\d+) begins shift/';
$formattedPlanning = [];
$totalsByGuard = [];
foreach ($data as $row) {
    $matches = [];
    preg_match($regexForDate, $row, $matches);
    list(, $month, $day, $hour, $minute, $text) = $matches;
    $minute = (int)$minute;

    if ($hour !== '00' && ($text === 'falls asleep' || $text === 'wakes up')) {
        say('problem! '.$row);
        // we happen to never come here, which will make our life easier
    }

    if (preg_match($regexForGuardId, $text, $matches)) { // new guard begins shift
        // end previous guard's shift
        if (isset($guardId)) {
            $formattedPlanning[$guardId] = $thisGuardNight;
        }
        // begin new guard's shift
        $guardId = $matches[1];
        if (!isset($formattedPlanning[$guardId])) {
            $formattedPlanning[$guardId] = array_fill(0, 60, 0);
        }
        $thisGuardNight = $formattedPlanning[$guardId];
        continue;
    } elseif ($text === 'falls asleep') {
        $fellAsleepAt = $minute;
    } elseif ($text === 'wakes up') {
        $awakeAt = $minute;
        for ($i = $fellAsleepAt ; $i < $awakeAt ; $i++) {
            $thisGuardNight[$i] += 1;
        }
        if (!isset($totalsByGuard[$guardId])) {
            $totalsByGuard[$guardId] = 0;
        }
        $totalsByGuard[$guardId] += ($awakeAt - $fellAsleepAt);
        unset($fellAsleepAt);
        unset($awakeAt);
    }
}

list($maxGuardId, $maxMinutesSlept) = getMaxValueAndKey($totalsByGuard);
list($betterMinute, $maxMinutesSleptAtThatTime) = getMaxValueAndKey($formattedPlanning[$maxGuardId]); 

say('result is:' . $maxGuardId*$betterMinute);
