<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// extract points 
$points = [];
const EXTRACT = '/position=<\s?(-?\d+),\s+(-?\d+)> velocity=<\s?(-?\d+),\s+(-?\d+)>/';
$minX = null;
$maxX = null;
$minY = null;
$maxY = null;
foreach (explode(PHP_EOL, $input) as $row) {
    $matches = [];
    preg_match(EXTRACT, $row, $matches);
    list(, $x, $y, $vx, $vy) = $matches;
    $points[] = new Point($x, $y, $vx, $vy);
    if ($x < $minX) {
        $minX = $x;
    }
    if ($x > $maxX) {
        $maxX = $x;
    }
    if ($y < $minY) {
        $minY = $y;
    }
    if ($y > $maxY) {
        $maxY = $y;
    }
}
say("width:".($maxX - $minX));
say("height:".($maxY - $minY));

class Point
{
    private $x;
    private $y;

    private $vx;
    private $vy;

    public function __construct($x, $y, $vx, $vy)
    {
        $this->x = $x;
        $this->y = $y;
        $this->vy = $vy;
        $this->vx = $vx;
    }
}