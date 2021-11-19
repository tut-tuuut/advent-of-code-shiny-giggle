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


def find_bug_candidates(parsed_program):
    # execute the program once and note every jmp and nop instructions
    # along with the value of accumulator when we execute them.
    instruction_pointer = 0
    accumulator = 0
    executed_instructions = set()
    bug_candidates = set()
    while instruction_pointer not in executed_instructions:
        executed_instructions.add(instruction_pointer)
        instruction, argument = parsed_program[instruction_pointer]
        # print(accumulator, instruction, argument)
        if instruction == "jmp":
            if argument != 1:
                bug_candidates.add((instruction_pointer, accumulator))
            instruction_pointer += argument
            continue
        if instruction == "acc":
            # print("hoho")
            accumulator += argument
            instruction_pointer += 1
            continue
        if instruction == "nop":
            if argument != 1:
                bug_candidates.add((instruction_pointer, accumulator))
            instruction_pointer += 1
            continue
    return bug_candidates


def execute_program_until_the_end_or_the_bug(
    parsed_program, starting_instruction_pointer, starting_accumulator
):
    instruction_pointer = starting_instruction_pointer
    accumulator = starting_accumulator
    executed_instructions = set()
    while instruction_pointer not in executed_instructions:
        if instruction_pointer >= len(parsed_program):
            return (True, accumulator)
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
    return (False, accumulator)


def annihilate_the_bug_and_run_the_program_for_real(program):
    bug_candidates = find_bug_candidates(program)
    for starting_pointer, starting_accumulator in bug_candidates:
        # print(starting_pointer, starting_accumulator)
        new_program = program.copy()
        # this is where we fix the program: replace jmp with nop:
        instruction, argument = new_program[starting_pointer]
        if instruction == "jmp":
            new_program[starting_pointer] = ("nop", argument)
        elif instruction == "nop":
            new_program[starting_pointer] = ("jmp", argument)
        else:
            print(
                "WRONG BOUUUHHH AAAHHH BLUUUH"
            )  # ↑ do NOT write this in production code, kids.
        # then we check if the modification has fixed the bug:
        finished, accumulator = execute_program_until_the_end_or_the_bug(
            new_program, starting_pointer, starting_accumulator
        )
        if finished:
            # If the program has runned to the end,
            # return accumulator which is what the puzzle asked for.
            return accumulator


u.assert_equals(annihilate_the_bug_and_run_the_program_for_real(example_proogram), 8)

u.answer_part_2(annihilate_the_bug_and_run_the_program_for_real(my_program))
