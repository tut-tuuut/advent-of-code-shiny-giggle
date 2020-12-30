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

my_registers = execute_program(raw_input)
u.assert_equals(my_registers[0], 1568)
u.answer_part_1(my_registers[0])

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# this is waaaayyyyyyyy to slow:
# my_registers = execute_program(raw_input, 1)
# u.answer_part_2(my_registers[0])


def pythoned_program(initial_register_zero):
    # registers:
    #  1  2  3  4  5
    z, u, d, t, q, c = initial_register_zero, 0, 0, 0, 0, 0
    # 00. addi 2 16 2 => Goto 17
    d += 16
    d += 1

    # 17. addi 1 2 1
    u += 2
    # 18. mulr 1 1 1
    u = u * u
    # 19. mulr 2 1 1
    u = 19 * u  # normally here d == 19
    # 20. muli 1 11 1
    u *= 11
    # 21. addi 4 2 4
    q += 4
    # 22. mulr 4 2 4
    q = q * 22  # normally here d == 22 always
    # 23. addi 4 12 4
    q += 4
    # 24. addr 1 4 1
    u = u + q
    # 25. addr 2 0 2
    d += z
    # => if z == 0, just continue to 26

    # 26. seti 0 9 2
    d = 0
    # => goto to 1

    # 01. seti 1 8 5
    c = 1

    # 02. seti 1 0 3
    t = 1

    # 03. mulr 5 3 4
    q = c * t

    # 04. eqrr 4 1 4
    q = int(q == u)
    # 05. addr 4 2 2
    # 06. addi 2 1 2
    # 07. addr 5 0 0
    # 08. addi 3 1 3
    # 09. gtrr 3 1 4
    # 10. addr 2 4 2
    # 11. seti 2 1 2
    # 12. addi 5 1 5
    # 13. gtrr 5 1 4
    # 14. addr 4 2 2
    # 15. seti 1 1 2
    # 16. mulr 2 2 2

    # 27. setr 2 3 4
    # 28. mulr 4 2 4
    # 29. addr 2 4 4
    # 30. mulr 2 4 4
    # 31. muli 4 14 4
    # 32. mulr 4 2 4
    # 33. addr 1 4 1
    # 34. seti 0 1 0
    # 35. seti 0 4 2


pythoned_program(0)