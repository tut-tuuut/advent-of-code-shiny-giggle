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


def parse_input_to_program(raw_input):
    memory = defaultdict(lambda: 0)
    for line in raw_input.splitlines():
        if line.startswith("mask"):
            mask = line[7:]
        elif line.startswith("mem"):
            address, value = tuple(map(int, re.findall(MEMORY_INSTRUCTION, line)[0]))
            for i, mask_val in enumerate(reversed(mask)):
                if mask_val == "1":
                    value = value | 2 ** i
                elif mask_val == "0":
                    value = value & (int("1" * 35, 2) - 2 ** i)
            memory[address] = value
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
            floating_bits = set()
            target_addresses = set()
            for i, mask_val in enumerate(reversed(mask)):
                if mask_val == "1":
                    address = address | 2 ** i
                elif mask_val == "X":
                    floating_bits.add(i)
            for values in itertools.product(*[[0, 1]] * len(floating_bits)):
                target_address = address
                for index, value in zip(floating_bits, values):
                    if value == 1:
                        target_address = target_address | 2 ** index
                    elif value == 0:
                        target_address = target_address & (
                            int("1" * 35, 2) - 2 ** index
                        )
                target_addresses.add(target_address)
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