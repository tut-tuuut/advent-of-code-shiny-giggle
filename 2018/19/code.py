import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

with open(__file__ + ".example.txt", "r+") as file:
    example_input = file.read()
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def execute_program(raw_program: str):
    program = raw_program.splitlines()
    ip_idx = int(program.pop(0)[4])
    register = [0] * 6
    ip = register[ip_idx]
    while True:
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
            if register[a] == register[b]:
                register[c] = 1
            else:
                register[c] = 0
        elif instruction == "gtrr":
            # sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0
            if register[a] > register[b]:
                register[c] = 1
            else:
                register[c] = 0
        else:
            u.red(f"unknown instruction {instruction}")
            break
        new_ip = register[ip_idx] + 1
        if new_ip >= len(program):
            break
        register[ip_idx] = new_ip
        ip = new_ip
    return register


example_registers = execute_program(example_input)
u.assert_equals(example_registers, [6, 5, 6, 0, 0, 9])
my_registers = execute_program(raw_input)
u.answer_part_1(my_registers[0])
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
