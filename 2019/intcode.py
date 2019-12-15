import itertools as it

class Computer:
    OPCODE_STOP = 99
    OPCODE_ADD = 1
    OPCODE_MULTIPLY = 2
    OPCODE_INPUT = 3
    OPCODE_OUTPUT = 4
    OPCODE_JUMPIFTRUE = 5
    OPCODE_JUMPIFFALSE = 6
    OPCODE_LESSTHAN = 7
    OPCODE_EQUALS = 8
    OPCODE_ADJUST_RELATIVE_BASE = 9

    def __init__(self, program):
        self.program = program
        self.i = 0 # instruction pointer
        self.rb = 0 # relative base
        self.verbose = False

    @classmethod
    def str_to_program(self, strProgram):
        return list(map(int, strProgram.split(',')))

    def run(self, inputs):
        inputs = iter(inputs)
        while self.i < len(self.program):
            if (self.verbose):
                print(f'instruction pointer {self.i}')
            instruction = str(self.program[self.i])
            if (self.verbose):
                print(f'instruction: {instruction}')
            opcode = int(instruction[-2:])
            params = self.get_params_values(instruction)
            if opcode == self.OPCODE_STOP:
                return None
            elif opcode == self.OPCODE_ADD:
                target = int(self.program[self.i+3])
                if self.verbose:
                    print('will store something in address #{target}')
                self.program[target] = params[0] + params[1]
                if self.verbose:
                    print(f'stored {self.program[target]} at address #{target}')
                self.i += 4
            elif opcode == self.OPCODE_MULTIPLY:
                target = self.program[self.i+3]
                self.program[target] = params[0] * params[1]
                self.i += 4
            elif opcode == self.OPCODE_INPUT:
                inputvalue = next(inputs)
                target = self.program[self.i+1]
                self.program[target] = inputvalue
                self.i += 2
            elif opcode == self.OPCODE_OUTPUT:
                output = params[0]
                self.i += 2
                yield output
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
                target = self.program[self.i+3]
                if params[0] < params[1]:
                    self.program[target] = 1
                else:
                    self.program[target] = 0
                self.i += 4
            elif opcode == self.OPCODE_EQUALS:
                target = self.program[self.i+3]
                if params[0] == params[1]:
                    self.program[target] = 1
                else:
                    self.program[target] = 0
                self.i += 4
            elif opcode == self.OPCODE_ADJUST_RELATIVE_BASE:
                self.rb += params[0]
                if self.verbose:
                    print(f'adjust relative base to {self.rb} (added {params[0]})')
                self.i += 2

    def get_params_values(self, strInstructions):
        strInstructions = strInstructions.rjust(5, '0')
        opcode = int(strInstructions[-2:])
        params = []
        nbParameters = 0
        if opcode in (self.OPCODE_ADD, self.OPCODE_MULTIPLY, self.OPCODE_EQUALS, self.OPCODE_LESSTHAN):
            nbParameters = 3
        elif opcode in (self.OPCODE_JUMPIFFALSE, self.OPCODE_JUMPIFTRUE):
            nbParameters = 2
        elif opcode in (self.OPCODE_OUTPUT, self.OPCODE_INPUT, self.OPCODE_ADJUST_RELATIVE_BASE):
            nbParameters = 1
        for p in range(1, nbParameters+1):
            if strInstructions[-p-2] == '0':
                address = int(self.program[self.i+p])
                if address >= len(self.program):
                    self.program.extend( it.repeat(0, 1 + address - len(self.program)) )
                if self.verbose:
                    print(f'looking for something at address {address}')
                value = self.program[address]
            elif strInstructions[-p-2] == '2':
                address = self.rb + int(self.program[self.i+p])
                if address >= len(self.program):
                    self.program.extend( it.repeat(0, 1 + address - len(self.program)) )
                value = self.program[address]
            else:
                value = self.program[self.i+p]
            params.append(value)
        return list(map(int,params))