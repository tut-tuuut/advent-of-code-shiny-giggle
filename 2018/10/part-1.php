<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// extract points 
$points = [];
const EXTRACT = '/position=<\s?(-?\d+),\s+(-?\d+)> velocity=<\s?(-?\d+),\s+(-?\d+)>/';
$minX = 999999999999;
$maxX = -999999999999;
$minY = 999999999999;
$maxY = -999999999999;
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
say("initial width and height: ".($maxX - $minX).' x '.($maxY - $minY));

$minWidth = $maxX - $minX;
$minHeight = $maxY - $minY;
$minX = 99999999999;
$minY = 99999999999;
for ($j = 0; $j < 10500; $j++) {
    list($width, $height) = moveEveryPointAndGetDimensions($points);
    if ($minWidth > $width) {
        $width = $minWidth;
    } else {
        say('min width reached:'.$minWidth);
        say('at '.$j.' seconds!');
        list($width, $height, $minX, $minY) = moveEveryPointAndGetDimensions($points, -1);
        drawEveryPoint($points, $width, $height, $minX, $minY);
        break;
    }
    if ($minHeight > $height) {
        $minHeight = $height;
    } else {
        say('min height reached:'.$minHeight);
        say('at '.$j.' seconds!');
        list($width, $height, $minX, $minY) = moveEveryPointAndGetDimensions($points, -1);
        drawEveryPoint($points, $width, $height, $minX, $minY);
        break;
    }
}

function drawEveryPoint(&$points, $width, $height, $minX, $minY, $filename = 'image.png')
{
    $img = imagecreatetruecolor($width + 10, $height + 10);
    if (!$img) {
        var_dump($width);
        var_dump($height);
        die;
    }
    $bg = imagecolorallocate($img, 255, 255, 255);
    $pointColor = imagecolorallocate($img, rand(50, 200), rand(50, 250), rand(50, 250));
    foreach ($points as $point) {
        $point->draw($img, $pointColor, $minX, $minY);
    }
    imagepng($img, $filename);
}

function moveEveryPointAndGetDimensions(&$points, $number = 1)
{
    $minX = 999999999999;
    $maxX = -999999999999;
    $minY = 999999999999;
    $maxY = -999999999999;
    foreach ($points as $point) {
        list($x, $y) = $point->move($number);
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
    return [$maxX - $minX, $maxY - $minY, $minX, $minY];
}

class Point
{
    private $x;
    private $y;

    private $vx;
    private $vy;

    public function __construct($x, $y, $vx, $vy)
    {
        $this->x = (int)$x;
        $this->y = (int)$y;
        $this->vy = (int)$vy;
        $this->vx = (int)$vx;
    }

    public function move($i = 1)
    {
        $this->x += $i*$this->vx;
        $this->y += $i*$this->vy;
        return [$this->x, $this->y];
    }

    public function draw($img, $color, $minX, $minY)
    {
        //say("draw point at ".$this->x." with minimal X of ".$minX);
        imagefilledellipse($img, $this->x - $minX + 5, $this->y - $minY + 5, 1, 1, $color);
    }
}