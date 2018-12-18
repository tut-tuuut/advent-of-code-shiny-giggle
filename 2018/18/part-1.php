<?php

use League\CLImate\CLImate;

include(__DIR__.'/../../vendor/autoload.php');
include(__DIR__.'/../../utils.php');

$inputFile = $argv[1];
$cli = new CLImate();

if (!$inputFile || !is_file(__DIR__.'/'.$inputFile)) {
    $cli->red('Please provide a valid file name.');
    die;
}

const TREES = '|';
const OPEN = '.';
const LUMBER = '#';

// Parse input… --------------------------------------------------------------
$grid = [];
foreach(explode(PHP_EOL, file_get_contents(__DIR__.'/'.$inputFile)) as $inputRow) {
    $grid[] = str_split($inputRow);
}

// debug constructed grid
foreach ($grid as $row) {
    $cli->out(implode('', $row));
}
