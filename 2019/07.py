import itertools as it


class IntcodeProgram:
    OPCODE_STOP = 99
    OPCODE_ADD = 1
    OPCODE_MULTIPLY = 2
    OPCODE_INPUT = 3
    OPCODE_OUTPUT = 4
    OPCODE_JUMPIFTRUE = 5
    OPCODE_JUMPIFFALSE = 6
    OPCODE_LESSTHAN = 7
    OPCODE_EQUALS = 8

    def __init__(self, program):
        self.program = program
        self.i = 0

    @classmethod
    def str_to_program(self, strProgram):
        return list(map(int, strProgram.split(",")))

    def run(self, inputs):
        inputs = iter(inputs)
        while self.i < len(self.program):
            instruction = str(self.program[self.i])
            opcode = int(instruction[-2:])
            params = self.get_params_values(instruction)
            if opcode == self.OPCODE_STOP:
                return None
            elif opcode == self.OPCODE_ADD:
                target = int(self.program[self.i + 3])
                self.program[target] = params[0] + params[1]
                self.i += 4
            elif opcode == self.OPCODE_MULTIPLY:
                target = self.program[self.i + 3]
                self.program[target] = params[0] * params[1]
                self.i += 4
            elif opcode == self.OPCODE_INPUT:
                inputvalue = next(inputs)
                target = self.program[self.i + 1]
                self.program[target] = inputvalue
                self.i += 2
            elif opcode == self.OPCODE_OUTPUT:
                output = params[0]
                self.i += 2
                return output
            elif opcode == self.OPCODE_JUMPIFTRUE:
                if params[0] != 0:
                    self.i = params[1]
                else:
                    self.i += 3
            elif opcode == self.OPCODE_JUMPIFFALSE:
                if params[0] == 0:
                    self.i = params[1]
                else:
                    self.i += 3
            elif opcode == self.OPCODE_LESSTHAN:
                target = self.program[self.i + 3]
                if params[0] < params[1]:
                    self.program[target] = 1
                else:
                    self.program[target] = 0
                self.i += 4
            elif opcode == self.OPCODE_EQUALS:
                target = self.program[self.i + 3]
                if params[0] == params[1]:
                    self.program[target] = 1
                else:
                    self.program[target] = 0
                self.i += 4

    def get_params_values(self, strInstructions):
        strInstructions = strInstructions.rjust(5, "0")
        opcode = int(strInstructions[-2:])
        params = []
        nbParameters = 0
        if opcode in (
            self.OPCODE_ADD,
            self.OPCODE_MULTIPLY,
            self.OPCODE_EQUALS,
            self.OPCODE_LESSTHAN,
        ):
            nbParameters = 3
        elif opcode in (self.OPCODE_JUMPIFFALSE, self.OPCODE_JUMPIFTRUE):
            nbParameters = 2
        elif opcode in (self.OPCODE_OUTPUT, self.OPCODE_INPUT):
            nbParameters = 1
        for p in range(1, nbParameters + 1):
            if strInstructions[-p - 2] == "0":
                address = int(self.program[self.i + p])
                value = self.program[address]
            else:
                value = self.program[self.i + p]
            params.append(value)
        return list(map(int, params))


with open(__file__ + ".input") as file:
    my_provided_program = file.read()

"""
def get_thruster_signal(program, phaseSettings):
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
"""


def get_thruster_signal_with_feedback_loop(strProgram, phaseSettings):
    previousOutput = 0
    programs = list(
        map(
            lambda x: IntcodeProgram(IntcodeProgram.str_to_program(strProgram)),
            range(0, 5),
        )
    )
    k = 0
    for i in phaseSettings:
        output = programs[k].run((i, previousOutput))
        if output == None:
            break
        previousOutput = output
        k += 1
    for k in it.count():
        output = programs[k % 5].run((previousOutput, previousOutput))
        if output == None:
            break
        previousOutput = output
        if k > 100:
            break
    return previousOutput


with open(__file__ + ".input") as file:
    inputprog = file.read()

maxThrusterSignal = 0
for phaseSettings in it.permutations(range(5, 10)):
    thrusterSignal = get_thruster_signal_with_feedback_loop(inputprog, phaseSettings)
    if thrusterSignal > maxThrusterSignal:
        maxThrusterSignal = thrusterSignal
print(f"part 2: {maxThrusterSignal}")
