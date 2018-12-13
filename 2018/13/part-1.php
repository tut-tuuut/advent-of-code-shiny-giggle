<?php

include(__DIR__.'/../../utils.php');

const NORTH = 1; // 0001
const EAST = 2;  // 0010
const SOUTH = 4; // 0100
const WEST = 8;  // 1000

$map = [];
$carts = [];
foreach(explode(PHP_EOL, file_get_contents(__DIR__.'/input.txt')) as $x => $inputRow) {
    $mapRow = [];
    foreach(str_split($inputRow) as $index => $char) {
        if ($char === '-' || $char === '<' || $char === '>') {
            $mapRow[] = EAST+WEST;
            if ($char !== '-') {
                $carts[] = new MineCart($x, $index, $char);
            }
        } elseif ($char === '|' || $char === '^' || $char === 'v') {
            $mapRow[] = NORTH+SOUTH;
            if ($char !== '-') {
                $carts[] = new MineCart($x, $index, $char);
            }
        } elseif ($char === '+') {
            $mapRow[] = NORTH+SOUTH+EAST+WEST;
        } elseif ($char === '/') {
            // it can be a south+east or north+west loop:
            //               /----            |
            //               |            ----/
            // we can determine which one it is by looking only at previous character!
            if (isset($mapRow[$index - 1]) && (($mapRow[$index - 1] & EAST) > 0)) {
                // previous character is open on the east, it's a NW loop
                $mapRow[] = NORTH+WEST;
            } else {
                $mapRow[] = SOUTH+EAST;
            }
        } elseif ($char === '\\') {
            // it can be a south+west or north+east loop:
            //            ---\            |
            //               |            \----
            // we can determine which one it is by looking only at previous character!
            if (isset($mapRow[$index - 1]) && (($mapRow[$index - 1] & EAST) > 0)) {
                // previous character is open on the east, it's a SW loop
                $mapRow[] = SOUTH+WEST;
            } else {
                $mapRow[] = NORTH+EAST;
            }
        } else {
            $mapRow[] = 0;
        }
    }
    $map[] = $mapRow;
}

$d = new MapDrawer();
$d->drawMap($map);

class MineCart
{
    private $x;
    private $y;

    public function construct($x, $y, $char)
    {
        $this->x = $x;
        $this->y = $y;
    }
}

class MapDrawer
{
    private $directions = [
        NORTH+EAST => '╰',
        NORTH+WEST => '╯',
        NORTH+SOUTH => '|',
        SOUTH+EAST => '╭',
        SOUTH+WEST => '╮',
        EAST+WEST => '-',
        NORTH+SOUTH+EAST+WEST => '+',
        0 => ' ',
    ];
    public function drawMap(array $map)
    {
        $height = count($map)*7 + 10;
        $width = count($map[0])*7 + 10;
        $img = imagecreate($width, $height);
        $white = imagecolorallocate($img, 240, 240, 240);
        $dark = imagecolorallocate($img, 12, 12, 12);
        foreach ($map as $y => $row) {
            $output = '';
            foreach ($row as $x => $int) {
                $cx = $x*7 + 4 + 5;
                $cy = $y*7 + 4 + 6;

                if (($int & WEST) > 0) {
                    $x2 = $cx - 4;
                    $y2 = $cy;
                    imageline($img, $cx, $cy, $x2, $y2, $dark);
                }
                if (($int & EAST) > 0) {
                    $x2 = $cx + 4;
                    $y2 = $cy;
                    imageline($img, $cx, $cy, $x2, $y2, $dark);
                }
                if (($int & SOUTH) > 0) {
                    $x2 = $cx;
                    $y2 = $cy + 4;
                    imageline($img, $cx, $cy, $x2, $y2, $dark);
                }
                if (($int & NORTH) > 0) {
                    $x2 = $cx;
                    $y2 = $cy - 4;
                    imageline($img, $cx, $cy, $x2, $y2, $dark);
                }
            }
        }
        imagepng($img, 'map.png');
    }
}