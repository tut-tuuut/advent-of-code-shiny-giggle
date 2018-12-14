<?php

include(__DIR__.'/../../utils.php');

const NORTH = 1; // 0001
const EAST = 2;  // 0010
const SOUTH = 4; // 0100
const WEST = 8;  // 1000
const INTERSECTION = 15; // 1111

$map = [];
$carts = [];
foreach(explode(PHP_EOL, file_get_contents(__DIR__.'/input.txt')) as $y => $inputRow) {
    $mapRow = [];
    foreach(str_split($inputRow) as $x => $char) {
        if ($char === '-' || $char === '<' || $char === '>') {
            $mapRow[] = EAST+WEST;
            if ($char !== '-') {
                $carts[] = new MineCart($x, $y, $char);
            }
        } elseif ($char === '|' || $char === '^' || $char === 'v') {
            $mapRow[] = NORTH+SOUTH;
            if ($char !== '|') {
                $carts[] = new MineCart($x, $y, $char);
            }
        } elseif ($char === '+') {
            $mapRow[] = NORTH+SOUTH+EAST+WEST;
        } elseif ($char === '/') {
            // it can be a south+east or north+west loop:
            //               /----            |
            //               |            ----/
            // we can determine which one it is by looking only at previous character!
            if (isset($mapRow[$x - 1]) && (($mapRow[$x - 1] & EAST) > 0)) {
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
            if (isset($mapRow[$x - 1]) && (($mapRow[$x - 1] & EAST) > 0)) {
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
$d->drawMapAndCarts($map, $carts, 'map-initial.png');
foreach(integers(20) as $integer) {
    foreach ($carts as $cart) {
        $cart->move($map);
    }
    $d->drawMapAndCarts($map, $carts, "map-$integer.png");
}

class MineCart
{
    static private $clockWiseDirections = [
        NORTH,
        EAST,
        SOUTH,
        WEST
    ];
    static private $turns = [
        -1, // turn left : from N you go to W
        +0, // no direction change
        +1, // turn right : from N you go to E
    ];

    private $x;
    private $y;
    private $direction;
    private $numberOfIntersections = 0;

    public function __construct($x, $y, $char)
    {
        $this->x = $x;
        $this->y = $y;
        if ($char === '<') {
            $this->direction = WEST;
        } elseif ($char === '>') {
            $this->direction = EAST;
        } elseif ($char === '^') {
            $this->direction = NORTH;
        } elseif ($char === 'v') {
            $this->direction = SOUTH;
        }
    }

    public function move($map)
    {
        $place = $map[$this->y][$this->x];
        if ($place === INTERSECTION) {
            $this->crossIntersection();
        } elseif (($place & $this->direction) > 0) {
            $this->moveInDirection();
        } else {
            $this->followLoop($place);
        }
    }

    public function getDirection()
    {
        return $this->direction;
    }

    public function getXY()
    {
        return [$this->x, $this->y];
    }

    private function moveInDirection()
    {
        if ($this->direction === NORTH) {
            $this->y -= 1;
        } elseif ($this->direction === SOUTH) {
            $this->y += 1;
        } elseif ($this->direction === EAST) {
            $this->x += 1;
        } elseif ($this->direction === WEST) {
            $this->x -= 1;
        }
    }

    private function crossIntersection()
    {
        // calculate direction change, then
        $this->moveInDirection();
    }

    private function followLoop($place)
    {
        // calculate direction change, then
        $this->moveInDirection();
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

    private $img;
    private $bg;
    private $rails;
    private $cartColors = [];

    public function drawMapAndCarts($map, $carts, $outputFile = 'map.png')
    {
        $height = count($map)*7 + 10;
        $width = count($map[0])*7 + 10;
        $this->img = $img = imagecreate($width, $height);
        $this->bg = imagecolorallocate($img, 240, 240, 240);
        $this->rails = imagecolorallocate($img, 12, 12, 12);
        if (empty($cartColors)) {
            foreach ($carts as $cartNb => $cart) {
                $this->cartColors[$cartNb] = imagecolorallocate($img, rand(100,200), rand(100,200), rand(100,200));
            }
        }
        $this->drawMap($map);
        $this->drawCarts($carts);
        imagepng($img,$outputFile);
    }

    private function drawMap(array $map)
    {
        $dark = $this->rails;
        $img = $this->img;
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
    }

    private function drawCarts(array $carts)
    {
        foreach ($carts as $index => $cart) {
            list($x, $y) = $cart->getXY();
            say("cart at $x, $y");
            $cx = $x*7 + 4 + 5;
            $cy = $y*7 + 4 + 6;
            if ($cart->getDirection() === NORTH) {
                $points = [
                    $cx, $cy - 4,
                    $cx-4, $cy+3,
                    $cx+4, $cy+3,
                ];
            } elseif ($cart->getDirection() === SOUTH) {
                $points = [
                    $cx, $cy + 4,
                    $cx-4, $cy-3,
                    $cx+4, $cy-3,
                ];
            } elseif ($cart->getDirection() === EAST) {
                $points = [
                    $cx + 4, $cy,
                    $cx - 3, $cy + 4,
                    $cx - 3, $cy - 4,
                ];
            } elseif ($cart->getDirection() === WEST) {
                $points = [
                    $cx - 4, $cy,
                    $cx + 3, $cy + 4,
                    $cx + 3, $cy - 4,
                ];
            }
            imagefilledpolygon($this->img, $points, 3, $this->cartColors[$index]);
        }
    }
}