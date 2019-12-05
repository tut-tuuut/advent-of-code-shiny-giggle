def str_to_program(strProgram):
    return list(map(int, strProgram.split(',')))

def run_program(program):
    i = 0
    while i < len(program):
        instruction = str(program[i])
        opcode = int(instruction[-2:])
        params = get_params_values(instruction, i, program)
        if opcode == 99:
            print(program)
            return program[0]
        elif opcode == 1:
            target = int(program[i+3])
            print(f'put {params[0]}+{params[1]} in address {target}')
            program[target] = params[0] + params[1]
            i += 4
        elif opcode == 2:
            target = program[i+3]
            print(f'put {params[0]}*{params[1]} in address {target}')
            program[target] = params[0] * params[1]
            i += 4
        elif opcode == 3:
            inputvalue = input(f'input for instruction {i} : ')
            target = program[i+1]
            program[target] = inputvalue
            i += 2
        elif opcode == 4:
            program[0] == 'toto'
            i += 2
    return program[0]

def get_params_values(strInstructions, i, listProgram):
    strInstructions = strInstructions.rjust(5, '0')
    opcode = int(strInstructions[-2:])
    params = []
    nbParameters = 0
    print(f'analyzing instruction {strInstructions}')
    if opcode <= 2:
        print(f'opcode = {opcode}')
        nbParameters = 3
    elif opcode <= 4:
        nbParameters = 1
    for p in range(1, nbParameters+1):
        if strInstructions[-p-2] == '0':
            address = int(listProgram[i+p])
            value = listProgram[address]
        else:
            value = listProgram[i+p]
        params.append(value)
    print(f'parameters : {params}')
    return list(map(int,params))

def pass_input_to_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

run_program(str_to_program('1002,4,3,4,33'))