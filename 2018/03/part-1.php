<?php

include('../utils.php');
include('input.php');

// generate the array representing the sheet
$sheet = [];
$sheetSize = 1000;
for ($i = 0; $i < $sheetSize; $i++) {
  $sheet[] = array_fill(0, $sheetSize, 0);
}

//$input = '#1 @ 1,3: 4x4
//#2 @ 3,1: 4x4
//#3 @ 5,5: 2x2';

$regex = '/\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/';
foreach(explode(PHP_EOL, $input) as $row) {
  $matches = [];
  preg_match($regex, $row, $matches);
  list(, $id, $x, $y, $width, $height) = $matches;
  for ($j = $y; $j < $y + $height; $j++) {
    for ($i = $x; $i < $x + $width; $i++) {
      $sheet[$j][$i] += 1;
    }
  }
}

// count square inches with a value >= 2
$total = 0;
foreach ($sheet as $row) {
  $total += count(array_filter($row, function($e) { return $e >= 2; }));
}
say('The result is: '.$total);
