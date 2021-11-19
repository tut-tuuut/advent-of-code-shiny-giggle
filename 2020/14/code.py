import re
import itertools
from collections import defaultdict

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_program = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

# mem[33783] = 33161
MEMORY_INSTRUCTION = re.compile(r"mem\[(\d+)\] = (\d+)")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def bits_from_integer(integer):
    bits = list(bin(integer)[2:])
    bits = ["0"] * (36 - len(bits)) + bits
    return list(reversed(bits))


def bits_to_integer(bits):
    bits = list(reversed(bits))
    return int("".join(bits), 2)


u.assert_equals(bits_to_integer(bits_from_integer(25)), 25, "bits_from/to_integer")

u.assert_equals(
    bits_to_integer(bits_from_integer(2 ** 36)), 2 ** 36, "bits_from/to_integer"
)


def parse_input_to_program(raw_input):
    memory = defaultdict(lambda: 0)
    for line in raw_input.splitlines():
        if line.startswith("mask"):
            mask = line[7:]
        elif line.startswith("mem"):
            address, value = tuple(map(int, re.findall(MEMORY_INSTRUCTION, line)[0]))
            bits = bits_from_integer(value)
            for i, mask_val in enumerate(reversed(mask)):
                if mask_val != "X":
                    bits[i] = mask_val
            memory[address] = bits_to_integer(bits)
    return sum(memory.values())


u.assert_equals(parse_input_to_program(example_program), 165)
u.assert_equals(parse_input_to_program(raw_input), 13496669152158)
u.answer_part_1(parse_input_to_program(raw_input))
# 13496669152158

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_input_to_program_v2(raw_input):
    memory = defaultdict(lambda: 0)
    for line in raw_input.splitlines():
        if line.startswith("mask"):
            mask = line[7:]
        elif line.startswith("mem"):
            address, target_value = tuple(
                map(int, re.findall(MEMORY_INSTRUCTION, line)[0])
            )
            bits = bits_from_integer(address)
            floating_bits = set()
            target_addresses = set()
            for i, mask_val in enumerate(mask[::-1]):
                if mask_val == "1":
                    bits[i] = "1"
                elif mask_val == "X":
                    floating_bits.add(i)
            for values in itertools.product(*[["0", "1"]] * len(floating_bits)):
                target_bits = bits.copy()
                for index, value in zip(floating_bits, values):
                    target_bits[index] = value
                target_addresses.add(bits_to_integer(target_bits))
            # print(
            #     f"writing {target_value} in {', '.join(map(str,sorted(target_addresses)))}"
            # )
            for target_address in target_addresses:
                memory[target_address] = target_value
    return sum(memory.values())


example_program_v2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

u.assert_equals(parse_input_to_program_v2(example_program_v2), 208)
u.answer_part_2(parse_input_to_program_v2(raw_input))

# 3279437161092 not the right answer
# 2851461851581 is too low
# 3278997609887 right answer for part 2
