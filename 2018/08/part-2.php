<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

//$input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2';
const IMG_WIDTH = 1000;

Node::setInput(array_map('parseInt', explode(' ', $input))); // save this in Node::somethingStatic

$node = new Node(0, 1);
say('PART2: ' . $node->getMetadataValue());
say('depth: '.Node::getTreeDepth());
say('width: '.count(explode(' ', $input)));
say('nb of nodes: '.Node::getNumberOfNodes());
$image = imagecreatetruecolor(IMG_WIDTH, 600);
imagecolorallocate($image, 0, 0, 0);
$node->draw($image);
imagepng($image, 'tree.png');

class Node
{
    private static $input = [];
    private static $treeWidth = 0;
    private static $depth = 0; // tree depth
    private static $nbOfNodes = 0;

    /** @var int */
    private $index; // place of the node header in $input
    private $level;
    private $children;

    public function __construct($index, $level)
    {
        //say("constructing node at index $index and level $level");
        $this->index = $index;
        $this->level = $level;
        if ($this->level > self::$depth) {
            self::$depth = $this->level;
        }
        self::$nbOfNodes++;
    }

    public function draw($image, $parentNode = null)
    {
        foreach ($this->children as $child) {
            if (count($this->children) > 1 and rand(1,20) === 7) {
                $child->draw($image, $this);
            } else {
                $child->draw($image);
            }
        }
        list($cx, $cy) = $this->getXY($childIndex);
        $color = imagecolorallocate($image, rand(50,250), rand(50, 250), rand(50, 250));
        if (!is_null($parentNode)) {
            list($px, $py) = $parentNode->getXY($childIndex);
            imageline($image , $cx , $cy , $px , $py , $color);
        }
        imageellipse($image, $cx , $cy , 4, 4, $color);
    }

    public function getXY($childIndex = 0)
    {
        if (is_null($this->cx)) {
            $this->cx = (int)(($this->index + $this->getLength() / 2) * IMG_WIDTH / self::$treeWidth + rand(0, $childIndex+$this->level) * 10 / $this->level);
            $this->cy = (int)(13 + $this->level * 70 + $cx/IMG_WIDTH*100 + 70*rand(0, $this->level)/$this->level);
        }
        return [$this->cx, $this->cy];
    }

    public static function getTreeDepth()
    {
        return self::$depth;
    }

    public static function getNumberOfNodes()
    {
        return self::$nbOfNodes;
    }

    public function getChildren()
    {
        if (!isset($this->children)) {
            $this->children = [];
            $nbOfChildren = self::$input[$this->index];
            //say("$this->index has $nbOfChildren children");
            if ($nbOfChildren === 0) {
                $this->children = [];
            } else {
                $newChildIndex = $this->index + 2;
                for ($i = 1; $i <= $nbOfChildren; $i++) {
                    $newChild = new Node($newChildIndex, $this->level + 1);
                    $newChildIndex += $newChild->getLength();
                    $this->children[] = $newChild;
                }
            }
        }
        return $this->children;
    }

    // length of header (2) + children + metadata
    public function getLength()
    {
        return $this->getChildrenLength() + 2 + self::$input[$this->index + 1];
        return $length;
    }

    public function getChildrenLength()
    {
        $length = 0;
        foreach ($this->getChildren() as $child) {
            $length += $child->getLength();
        }
        return $length;
    }

    public function getMetadataValue()
    {
        //say(str_repeat('-', $this->level).' calculating value of '.$this->index);
        $children = $this->getChildren();
        $metadata = array_slice(self::$input, $this->index + 2 + $this->getChildrenLength(), self::$input[$this->index + 1]);
        if (count($children) === 0) { // same as for part 2
            //say('value of '.$this->index.' is '.array_sum($metadata));
            return array_sum($metadata);
        } else {
            $value = 0;
            foreach ($metadata as $index) {
                //say('looking at child #'.$index.' of node '.$this->index);
                if (isset($children[$index-1])) {
                    $value += $children[$index-1]->getMetadataValue();
                }
            }
            return $value;
        }
    }

    public static function setInput($input)
    {
        self::$input = $input;
        self::$treeWidth = count($input);
    }
}
/*
say(
'
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
0hh---------------------------mmmmm
    2hh-mmmmmmmm 7hh--------m
                     9hh-mm');
*/