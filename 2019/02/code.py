def interpret_program(strProgram):
    program = list(map(int, strProgram.split(',')))
    for i in range(0, len(program), 4):
        instruction, param1, param2, target = program[i:i+4]
        if instruction == 99:
            break
        elif instruction == 1:
            program[target] = param1 + param2
        elif instruction == 2:
            program[target] = param1 * param2
    print(program)


interpret_program('1,9,10,3,2,3,11,0,99,30,40,50')