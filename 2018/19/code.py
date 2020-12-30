from time import time
from itertools import count
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

with open(__file__ + ".example.txt", "r+") as file:
    example_input = file.read()
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def execute_program(raw_program: str, initial_register_zero=0):
    program = raw_program.splitlines()
    ip_idx = int(program.pop(0)[4])
    register = [0] * 6
    register[0] = initial_register_zero
    ip = register[ip_idx]
    init_time = time()
    for i in count(1):
        if ip == 26:
            print(register[1])
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


example_registers = execute_program(example_input)
u.assert_equals(example_registers, [6, 5, 6, 0, 0, 9])

# my_registers = execute_program(raw_input)
# u.assert_equals(my_registers[0], 1568)
# u.answer_part_1(my_registers[0])

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# this is waaaayyyyyyyy to slow:
# my_registers = execute_program(raw_input, 1)
# u.answer_part_2(my_registers[0])


def pythoned_program(initial_register_zero):
    # registers:
    #  0  1  2  3  4  5 => zero un deux trois quatre cinq
    z, u, d, t, q, c = initial_register_zero, 0, 0, 0, 0, 0
    # 00. addi 2 16 2 => Goto 17

    # 17. addi 1 2 1
    u += 2
    # 18. mulr 1 1 1
    u *= u
    # 19. mulr 2 1 1
    u *= 19
    # 20. muli 1 11 1
    u *= 11
    # 21. addi 4 2 4
    q += 2
    # 22. mulr 4 2 4
    q *= 22
    # 23. addi 4 12 4
    q += 12
    # 24. addr 1 4 1
    u += q
    # 25. addr 2 0 2
    # u = 892  # q unrelevant here
    if z == 0:
        for divisor in range(1, u + 1):
            if u % divisor == 0:
                z += divisor
        return z
    if z == 1:
        # 27. setr 2 3 4
        q = 27
        # 28. mulr 4 2 4
        q = q * 28
        # 29. addr 2 4 4
        q = q + 29
        # 30. mulr 2 4 4
        q = 30 * q
        # 31. muli 4 14 4
        q = q * 14
        # 32. mulr 4 2 4
        q = q * 32
        # 33. addr 1 4 1
        u = u + q
        # 34. seti 0 1 0
        z = 0
        # 35. seti 0 4 2
        for divisor in range(1, u + 1):
            if u % divisor == 0:
                z += divisor
        return z


u.assert_equals(pythoned_program(0), 1568)
u.answer_part_2(pythoned_program(1))