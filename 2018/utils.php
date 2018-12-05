<?php

function say($something) {
    if (is_array($something)) {
        say (implode(' ', $something));
        return;
    }
    echo $something . PHP_EOL;
}