<?php

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

//$input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2';

Node::setInput(array_map('parseInt', explode(' ', $input))); // save this in Node::somethingStatic

$node = new Node(0, 1);
say('PART1: ' . $node->getMetadataSum());

class Node
{
    private static $input = [];

    /** @var int */
    private $index; // place of the node header in $input
    private $level;
    private $children;

    public function __construct($index, $level)
    {
        //say("constructing node at index $index and level $level");
        $this->index = $index;
        $this->level = $level;
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

    public function getMetadataSum()
    {
        $sum = 0;
        foreach ($this->getChildren() as $child) {
            $sum += $child->getMetadataSum();
        }
        $sum += $this->getMetadataValue();
        //say($this->index . ' has a metadata value of '. $sum);
        return $sum;
    }

    public function getMetadataValue()
    {
        return array_sum(array_slice(self::$input, $this->index + 2 + $this->getChildrenLength(), self::$input[$this->index + 1]));
    }

    public static function setInput($input)
    {
        self::$input = $input;
    }
}

//say(
//'2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
//0hh---------------------------mmmmm
//    2hh-mmmmmmmm 7hh--------m
//                     9hh-mm');
