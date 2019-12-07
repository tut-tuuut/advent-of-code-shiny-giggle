import itertools as it

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
            print('STOP')
            return None
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
            print(f'INPUT {inputvalue}')
            target = program[i+1]
            program[target] = inputvalue
            i += 2
        elif opcode == OPCODE_OUTPUT:
            print(f'OUTPUT {params[0]}')
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

with open(__file__ + '.input') as file:
    my_provided_program = file.read()


"""def get_thruster_signal(program, phaseSettings):
    previousOutput = 0
    for i in phaseSettings:
        output = run_program(program, (i, previousOutput))
        previousOutput = output
    return output

maxThrusterSignal = 0
for phaseSettings in it.permutations(range(0,5)):
    thrusterSignal = get_thruster_signal(str_to_program(my_provided_program), phaseSettings)
    if thrusterSignal > maxThrusterSignal:
        maxThrusterSignal = thrusterSignal
        print(f'thruster signal of {maxThrusterSignal} found for {phaseSettings}')
print(f'part 1: {maxThrusterSignal}')
"""
def get_thruster_signal_with_feedback_loop(program, phaseSettings):
    previousOutput = 0
    programs = list(map(lambda x: list(program), range(0,5)))
    k = 0
    for i in phaseSettings:
        output = run_program(programs[k], (i, previousOutput))
        if output == None:
            break
        previousOutput = output
        k += 1
    for k in it.count():
        output = run_program(programs[k%5], (phaseSettings[k%5], previousOutput))
        if output == None:
            print(f'BREAK at program {k%5}')
            break
        previousOutput = output
        if k%5 == 4:
            print(previousOutput)
        if k > 100:
            break
    return previousOutput

exampleprog = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
examplephase = [9,7,8,5,6]
print(get_thruster_signal_with_feedback_loop(exampleprog, examplephase))