OPCODE_STOP = 99
OPCODE_ADD = 1
OPCODE_MULTIPLY = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4
OPCODE_JUMPIFTRUE = 5
OPCODE_JUMPIFFALSE = 6
OPCODE_LESSTHAN = 7
OPCODE_EQUALS = 8

def str_to_program(strProgram):
    return list(map(int, strProgram.split(',')))

def run_program(program, inputs):
    i = 0
    inputs = iter(inputs)
    while i < len(program):
        instruction = str(program[i])
        opcode = int(instruction[-2:])
        params = get_params_values(instruction, i, program)
        if opcode == OPCODE_STOP:
            return program[0]
        elif opcode == OPCODE_ADD:
            target = int(program[i+3])
            program[target] = params[0] + params[1]
            i += 4
        elif opcode == OPCODE_MULTIPLY:
            target = program[i+3]
            program[target] = params[0] * params[1]
            i += 4
        elif opcode == OPCODE_INPUT:
            inputvalue = next(inputs)
            target = program[i+1]
            program[target] = inputvalue
            i += 2
        elif opcode == OPCODE_OUTPUT:
            output = params[0]
            return output
            i += 2
        elif opcode == OPCODE_JUMPIFTRUE:
            if params[0] != 0:
                i = params[1]
            else:
                i += 3
        elif opcode == OPCODE_JUMPIFFALSE:
            if params[0] == 0:
                i = params[1]
            else:
                i += 3
        elif opcode == OPCODE_LESSTHAN:
            target = program[i+3]
            if params[0] < params[1]:
                program[target] = 1
            else:
                program[target] = 0
            i += 4
        elif opcode == OPCODE_EQUALS:
            target = program[i+3]
            if params[0] == params[1]:
                program[target] = 1
            else:
                program[target] = 0
            i += 4

def get_params_values(strInstructions, i, listProgram):
    strInstructions = strInstructions.rjust(5, '0')
    opcode = int(strInstructions[-2:])
    params = []
    nbParameters = 0
    if opcode in (OPCODE_ADD, OPCODE_MULTIPLY, OPCODE_EQUALS, OPCODE_LESSTHAN):
        nbParameters = 3
    elif opcode in (OPCODE_JUMPIFFALSE, OPCODE_JUMPIFTRUE):
        nbParameters = 2
    elif opcode in (OPCODE_OUTPUT, OPCODE_INPUT):
        nbParameters = 1
    for p in range(1, nbParameters+1):
        if strInstructions[-p-2] == '0':
            address = int(listProgram[i+p])
            value = listProgram[address]
        else:
            value = listProgram[i+p]
        params.append(value)
    return list(map(int,params))

my_provided_program = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'

phaseSettings = (0,1,2,3,4)

def get_thruster_signal(strProgram, phaseSettings):
    previousOutput = 0
    for i in phaseSettings:
        output = run_program(str_to_program(my_provided_program), (i, previousOutput))
        previousOutput = output
    return output

print(get_thruster_signal(my_provided_program, phaseSettings))