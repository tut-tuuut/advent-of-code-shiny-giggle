<?php

include(__DIR__.'/../../utils.php');

const MATCH_BEFORE = '/Before: \[(\d+), (\d+), (\d+), (\d+)\]/';
const MATCH_INSTRUCTION = '/(\d+) (\d+) (\d+) (\d+)/';
const MATCH_AFTER = '/After:  \[(\d+), (\d+), (\d+), (\d+)\]/';

const OPCODES = [
    'addr', 'addi',
    'mulr', 'muli',
    'banr', 'bani',
    'borr', 'bori',
    'setr', 'seti',
    'gtir', 'gtri', 'gtrr',
    'eqir', 'eqri', 'eqrr',
];

$registers = [3, 2, 1, 1];
$mulr = applyOpCode('seti', 2, 1, 2, $registers);
say($mulr);

$examples = [];
$newExample = [];
foreach (explode(PHP_EOL, file_get_contents(__DIR__.'/input.txt')) as $inputRow) {
    $matches = [];
    if (preg_match(MATCH_BEFORE, $inputRow, $matches)) {
        $newExample = [];
        list(, $zero, $one, $two, $three) = $matches;
        $newExample['before'] = [(int)$zero, (int)$one, (int)$two, (int)$three];
    } elseif (preg_match(MATCH_AFTER, $inputRow, $matches)) {
        list(, $zero, $one, $two, $three) = $matches;
        $newExample['after'] = [(int)$zero, (int)$one, (int)$two, (int)$three];
        $examples[] = $newExample;
    } elseif (preg_match(MATCH_INSTRUCTION, $inputRow, $matches)) {
        list(, $opcode, $a, $b, $c) = $matches;
        $newExample['instruction'] = [(int)$opcode, (int)$a, (int)$b, (int)$c];
    };
}

unset($newExample);

$matchingExamples = 0;
foreach ($examples as $example) {
    $matchingPatterns = 0;
    $expected = implode(' ', $example['after']);
    list(, $a, $b, $c) = $example['instruction'];
    foreach (OPCODES as $opcode) {
        $obtained = applyOpCode($opcode, $a, $b, $c, $example['before']);
        if (implode(' ', $obtained) === $expected) {
            $matchingPatterns++;
        }
    }
    if ($matchingPatterns >= 3) {
        $matchingExamples++;
    }
}

say('[PART 1] '.$matchingExamples);

function applyOpCode($opcode, $a, $b, $c, $registers)
{
    // addr (add register) stores into register C
    // the result of adding register A and register B.
    if ($opcode === 'addr') {
        $registers[$c] = $registers[$a] + $registers[$b];
    }

    // addi (add immediate) stores into register C
    // the result of adding register A and value B.
    elseif ($opcode === 'addi') {
        $registers[$c] = $registers[$a] + $b;
    }

    // mulr (multiply register) stores into register C
    // the result of multiplying register A and register B.
    elseif ($opcode === 'mulr') {
        $registers[$c] = $registers[$a] * $registers[$b];
    }

    // muli (multiply immediate) stores into register C
    // the result of multiplying register A and value B.
    elseif ($opcode === 'muli') {
        $registers[$c] = $registers[$a] * $b;
    }

    // banr (bitwise AND register) stores into register C
    // the result of the bitwise AND of register A and register B.
    elseif ($opcode === 'banr') {
        $registers[$c] = $registers[$a] & $registers[$b];
    }

    // bani (bitwise AND immediate) stores into register C
    // the result of the bitwise AND of register A and value B.
    elseif ($opcode === 'bani') {
        $registers[$c] = $registers[$a] & $b;
    }

    // borr (bitwise OR register) stores into register C
    // the result of the bitwise OR of register A and register B.
    elseif ($opcode === 'borr') {
        $registers[$c] = $registers[$a] | $registers[$b];
    }

    // bori (bitwise OR immediate) stores into register C
    // the result of the bitwise OR of register A and value B.
    elseif ($opcode === 'bori') {
        $registers[$c] = $registers[$a] | $b;
    }

    // setr (set register) copies the contents of register A into register C.
    // (Input B is ignored.)
    elseif ($opcode === 'setr') {
        $registers[$c] = $registers[$a];
    }

    // seti (set immediate) stores value A into register C.
    // (Input B is ignored.)
    elseif ($opcode === 'seti') {
        $registers[$c] = $a;
    }

    // gtir (greater-than immediate/register) sets register C to 1
    // if value A is greater than register B.
    // Otherwise, register C is set to 0.
    elseif ($opcode === 'gtir') {
        $registers[$c] = ($a > $registers[$b]) ? 1 : 0;
    }

    // gtri (greater-than register/immediate) sets register C to 1
    // if register A is greater than value B.
    // Otherwise, register C is set to 0.
    elseif ($opcode === 'gtri') {
        $registers[$c] = ($registers[$a] > $b) ? 1 : 0;
    }

    // gtrr (greater-than register/register) sets register C to 1
    // if register A is greater than register B.
    // Otherwise, register C is set to 0.
    elseif ($opcode === 'gtrr') {
        $registers[$c] = ($registers[$a] > $registers[$b]) ? 1 : 0;
    }

    // eqir (equal immediate/register) sets register C to 1
    // if value A is equal to register B.
    // Otherwise, register C is set to 0.
    elseif ($opcode === 'eqir') {
        $registers[$c] = ($a === $registers[$b]) ? 1 : 0;
    }

    // eqri (equal register/immediate) sets register C to 1
    // if register A is equal to value B.
    // Otherwise, register C is set to 0.
    elseif ($opcode === 'eqri') {
        $registers[$c] = ($registers[$a] === $b) ? 1 : 0;
    }

    // eqrr (equal register/register) sets register C to 1
    // if register A is equal to register B.
    // Otherwise, register C is set to 0.
    elseif ($opcode === 'eqrr') {
        $registers[$c] = ($registers[$a] === $registers[$b]) ? 1 : 0;
    }

    return $registers;
}