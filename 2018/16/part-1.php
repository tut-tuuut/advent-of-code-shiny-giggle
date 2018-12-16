<?php

use League\CLImate\CLImate;

include(__DIR__.'/../../vendor/autoload.php');
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

// Parse Input...
$examples = [];
$program = [];
$newExample = [];
foreach (explode(PHP_EOL, file_get_contents(__DIR__.'/input.txt')) as $inputRow) {
    $matches = [];
    if (preg_match(MATCH_BEFORE, $inputRow, $matches)) {
        list(, $zero, $one, $two, $three) = $matches;
        $newExample['before'] = [(int)$zero, (int)$one, (int)$two, (int)$three];
    } elseif (preg_match(MATCH_AFTER, $inputRow, $matches)) {
        list(, $zero, $one, $two, $three) = $matches;
        $newExample['after'] = [(int)$zero, (int)$one, (int)$two, (int)$three];
        $examples[] = $newExample;
        $newExample = [];
    } elseif (preg_match(MATCH_INSTRUCTION, $inputRow, $matches)) {
        list(, $opcode, $a, $b, $c) = $matches;
        if (isset($newExample['before'])) {
            $newExample['instruction'] = [(int)$opcode, (int)$a, (int)$b, (int)$c];
        } else {
            $program[] = [(int)$opcode, (int)$a, (int)$b, (int)$c];
        }
    };
}

unset($newExample);

$opcodeNbCandidates = array_fill(0, 16, OPCODES);
$matchingExamples = 0;
foreach ($examples as $example) {
    $matchingPatterns = 0;
    $matching = [];
    $expected = implode(' ', $example['after']);
    list($opcodeNb, $a, $b, $c) = $example['instruction'];
    foreach (OPCODES as $opcode) {
        $obtained = applyOpCode($opcode, $a, $b, $c, $example['before']);
        if (implode(' ', $obtained) === $expected) {
            $matchingPatterns++;
            $matching[] = $opcode;
        }
    }
    // Do part 1: how many examples behave like 3 or more opcodes?
    if ($matchingPatterns >= 3) {
        $matchingExamples++;
    }
    // Part 2: use examples to know which opcode has which number
    $opcodeNbCandidates[$opcodeNb] = array_intersect($opcodeNbCandidates[$opcodeNb], $matching);
}

say('[PART 1] '.$matchingExamples.' examples behaving like 3 opcodes or more');

// Part 2: find number of EVERY opcode
$opcodeNumbers = [];
$newopcodeCandidates = $opcodeNbCandidates;
while (count($opcodeNumbers) < 16) {
    foreach ($opcodeNbCandidates as $nb => $candidate) {
        if (count($candidate) === 1) {
            $opcodename = array_shift($candidate);
            $opcodeNumbers[$nb] = $opcodename;
            foreach ($newopcodeCandidates as $newNb => $newCandidate) {
                $newopcodeCandidates[$newNb] = array_filter($newCandidate, function($value) use ($opcodename) {
                    return $value !== $opcodename;
                });
            }
        }
    }
    $opcodeNbCandidates = $newopcodeCandidates;
}

// DONE. I have this in opcodeNumbers variable.

// Now, execute the program on the registers
$registers = [0, 0, 0, 0];
$cli = new CLImate();
foreach ($program as $progLine) {
    list($opcodeNumber, $a, $b, $c) = $progLine;
    $opcode = $opcodeNumbers[$opcodeNumber];
    $registers = applyOpCode($opcode, $a, $b, $c, $registers);
}

say('[PART 2] '.$registers[0].' in register #0 at the end');
// ------------- utilities --------------------------------------------
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