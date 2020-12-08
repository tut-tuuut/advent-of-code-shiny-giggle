import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_raw_program = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_program(program):
    return {i: (row[:3], int(row[4:])) for i, row in enumerate(program.splitlines())}


example_proogram = parse_program(example_raw_program)
# print(example_proogram)


def execute_program_until_instruction_runs_twice(parsed_program):
    instruction_pointer = 0
    accumulator = 0
    executed_instructions = set()
    while instruction_pointer not in executed_instructions:
        executed_instructions.add(instruction_pointer)
        instruction, argument = parsed_program[instruction_pointer]
        # print(accumulator, instruction, argument)
        if instruction == "jmp":
            instruction_pointer += argument
            continue
        if instruction == "acc":
            # print("hoho")
            accumulator += argument
            instruction_pointer += 1
            continue
        if instruction == "nop":
            instruction_pointer += 1
            continue
    return accumulator


u.assert_equals(execute_program_until_instruction_runs_twice(example_proogram), 5)

my_program = parse_program(raw_input)
u.answer_part_1(execute_program_until_instruction_runs_twice(my_program))


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
