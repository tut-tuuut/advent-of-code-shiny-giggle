def str_to_program(strProgram):
    return list(map(int, strProgram.split(",")))


def run_program(program):
    i = 0
    while i < len(program):
        instruction, param1, param2, target = program[i : i + 4]
        if instruction == 99:
            break
        elif instruction == 1:
            program[target] = program[param1] + program[param2]
            i += 4
        elif instruction == 2:
            program[target] = program[param1] * program[param2]
            i += 4
    return program[0]


def pass_input_to_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program


print("3500 expected:")
print(run_program(str_to_program("1,9,10,3,2,3,11,0,99,30,40,50")))

input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0"

program = pass_input_to_program(str_to_program(input), 12, 1)
print("Answer #1:")
print(run_program(program))


def find_input_to_match_output(expected, strProgram):
    for verb in range(100):
        for noun in range(100):
            if (
                run_program(
                    pass_input_to_program(str_to_program(strProgram), noun, verb)
                )
                == expected
            ):
                return verb, noun


verb, noun = find_input_to_match_output(19690720, input)
print(f"Answer #2: {100 * noun + verb}")
