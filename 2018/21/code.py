from time import time
from itertools import count

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def execute_program(raw_program: str, initial_register_zero=0):
    program = raw_program.splitlines()
    ip_idx = int(program.pop(0)[4])
    register = [0] * 6
    register[0] = initial_register_zero
    ip = register[ip_idx]
    init_time = time()
    first_time_at_twenty_eight = True
    answer_part_1 = 0
    times_at_twenty_eight = 0
    previous_q = 0
    already_seen = set()
    for i in count(1):
        if ip == 28:  # instruction where the program can halt
            q = register[4]
            times_at_twenty_eight += 1
            # part 2
            if q in already_seen:
                print("\n")
                print(f"already seen {q}!")
                u.answer_part_2(previous_q)
                register[ip_idx] = 31
                # answer 5885821
                # 3547.24 seconds
                # 2729303712 iterations
            else:
                print(f"{q:010} - {times_at_twenty_eight:04}", end="\r")
            previous_q = q
            already_seen.add(q)
            # part 1
            if times_at_twenty_eight == 1:
                answer_part_1 = q
                u.answer_part_1(q)
        row = program[ip]
        instruction = row[:4]
        a, b, c = map(int, row[5:].split())
        if instruction == "seti":  # stores value A into register C
            register[c] = a
        elif instruction == "addi":
            # stores into register C the result of adding register A and value B
            register[c] = register[a] + b
        elif instruction == "addr":
            # stores into register C the result of adding register A and register B.
            register[c] = register[a] + register[b]
        elif instruction == "setr":
            # copies the contents of register A into register C
            register[c] = register[a]
        elif instruction == "mulr":
            # stores into register C the result of multiplying register A and register B
            register[c] = register[a] * register[b]
        elif instruction == "muli":
            # stores into register C the result of multiplying register A and value B
            register[c] = register[a] * b
        elif instruction == "eqrr":
            # sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0
            register[c] = int(register[a] == register[b])
        elif instruction == "gtrr":
            # sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0
            register[c] = int(register[a] > register[b])
        elif instruction == "bani":
            # stores into register C the result of the bitwise AND of register A and value B
            register[c] = register[a] & b
        elif instruction == "bori":
            # stores into register C the result of the bitwise OR of register A and value B
            register[c] = register[a] | b
        elif instruction == "eqri":
            # sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0
            register[c] = int(register[a] == b)
        elif instruction == "gtir":
            # sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
            register[c] = int(a > register[b])
        else:
            u.red(f"unknown instruction {instruction}")
            break
        new_ip = register[ip_idx] + 1
        if new_ip >= len(program):
            break
        register[ip_idx] = new_ip
        ip = new_ip
    print(f"program took {time() - init_time:.2f} seconds / {i} iterations to execute")
    return register


def dump_program(input):
    for i, instruction in enumerate(raw_input.splitlines(), -1):
        print(f"#{i}. {instruction}")


execute_program(raw_input, 0)
