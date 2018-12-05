<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');


// Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!
// For example, in the claims above, only claim 3 is intact after all claims are made.
// What is the ID of the only claim that doesn't overlap?


// generate the array representing the sheet
$sheet = [];
$sheetSize = 1000;
for ($i = 0; $i < $sheetSize; $i++) {
  $sheet[] = array_fill(0, $sheetSize, []);
}

//$input = '#1 @ 1,3: 4x4
//#2 @ 3,1: 4x4
//#3 @ 5,5: 2x2';

$regex = '/\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/';
$idCandidates = [];
foreach(explode(PHP_EOL, $input) as $row) {
  $matches = [];
  preg_match($regex, $row, $matches);
  list(, $id, $x, $y, $width, $height) = $matches;
  $idCandidates[$id] = 'Oh oh oh';
  $overlaps = [];
  for ($j = $y; $j < $y + $height; $j++) {
    for ($i = $x; $i < $x + $width; $i++) {
      $sheet[$j][$i][] = $id;
      if (count($sheet[$j][$i]) > 1) {
        foreach ($sheet[$j][$i] as $overlappedId) {
          if(isset($idCandidates[$overlappedId])) {
            unset($idCandidates[$overlappedId]);
          }
        }
      }
    }
  }
}

say('result is: '.array_keys($idCandidates)[0]);
