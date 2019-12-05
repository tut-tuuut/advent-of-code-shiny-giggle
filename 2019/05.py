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

def run_program(program):
    i = 0
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
            inputvalue = input(f'. INPUT for instruction #{i}: ')
            target = program[i+1]
            program[target] = inputvalue
            i += 2
        elif opcode == OPCODE_OUTPUT:
            output = params[0]
            print(f'. OUTPUT instruction #{i}: {output}')
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
    return program[0]

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

def pass_input_to_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

my_provided_program = '3,225,1,225,6,6,1100,1,238,225,104,0,1102,7,85,225,1102,67,12,225,102,36,65,224,1001,224,-3096,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1001,17,31,224,1001,224,-98,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,86,19,225,1101,5,27,225,1102,18,37,225,2,125,74,224,1001,224,-1406,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,13,47,225,1,99,14,224,1001,224,-98,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1101,38,88,225,1102,91,36,224,101,-3276,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,59,76,224,1001,224,-135,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,90,195,224,1001,224,-112,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1102,22,28,225,1002,69,47,224,1001,224,-235,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,102,2,223,223,1006,224,329,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226'
run_program(str_to_program(my_provided_program))