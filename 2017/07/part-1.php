<?php

// Thoughts:
// For the first part, we can simply ignore "leaf" programs.
// We are looking for the root of the tree.

include(__DIR__.'/../../utils.php');
include(__DIR__.'/input.php');

// regex to get name, weight and children of programs
$regex = '/^(?<name>\w+) \((?<weight>\d+)\) -> (?<children>.+)/';
