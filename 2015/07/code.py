import re

class Instruction:
    def __init__(self, circuit, arg1, arg2):
        self.circuit = circuit
        self.arg1 = arg1
        self.arg2 = arg2
        print(f'initialize instruction {self.__class__.__name__} with args {arg1} and {arg2}')
    
    def getValue(self, arg):
        if (re.match(r'[a-z]+', arg)):
            return self.circuit.getValue(arg)
        elif (re.match(r'\d+',arg)):
            return int(arg)

class InstructionAnd(Instruction):
    def execute(self):
        value1 = self.getValue(self.arg1)
        value2 = self.getValue(self.arg2)
        return value1 & value2

class InstructionOr(Instruction):
    def execute(self):
        value1 = self.getValue(self.arg1)
        value2 = self.getValue(self.arg2)
        return value1 | value2

class InstructionLShift(Instruction):
    def execute(self):
        value1 = self.getValue(self.arg1)
        return value1 << int(self.arg2)

class InstructionRShift(Instruction):
    def execute(self):
        value1 = self.getValue(self.arg1)
        return value1 >> int(self.arg2)

class InstructionAssign(Instruction):
    def execute(self):
        value = self.getValue(self.arg1)
        print(f'assigned value is {value}')
        return value

class InstructionNot(Instruction):
    def execute(self):
        value = self.getValue(self.arg1)
        return value ^ 65535

class Circuit:
    def __init__(self):
        print('initialize an empty circuit')
        self.instructions = {}
        self.values = {}
    
    def getValue(self, wire):
        if wire not in self.values:
            print(f'calculate value of {wire}')
            self.values[wire] = self.instructions[wire].execute()
        return self.values[wire]

    def parseInstructions(self, instructionString):
        for instruction in filter(None, instructionString.split('\n')):
            print(instruction)
            target = re.findall(r'-> ([a-z]+)', instruction)[0]
            #print(f'target is {target}')
            if (instruction[0:3] == 'NOT' or re.match(r'([a-z\d]+) -> [a-z+]', instruction)):
                arg1 = re.findall(r'([a-z\d]+) ->', instruction)[0]
                if (instruction[0:3] == 'NOT'):
                    self.instructions[target] = InstructionNot(self, arg1, None)
                else:
                    self.instructions[target] = InstructionAssign(self, arg1, None)
            else:
                m = re.findall(r'([a-z\d+]+) (AND|OR|LSHIFT|RSHIFT) ([a-z\d]+) ->', instruction)
                arg1, operation, arg2 = m[0]
                if operation == 'AND':
                    self.instructions[target] = InstructionAnd(self, arg1, arg2)
                elif operation == 'OR':
                    self.instructions[target] = InstructionOr(self, arg1, arg2)
                elif operation == 'LSHIFT':
                    self.instructions[target] = InstructionLShift(self, arg1, int(arg2))
                elif operation == 'RSHIFT':
                    self.instructions[target] = InstructionRShift(self, arg1, int(arg2))
        #print(self.instructions)

s = """123 -> x
456 -> y
g AND y -> d
f OR y -> e
i LSHIFT 2 -> f
h RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

with open(__file__+'.input.txt', "r+") as file:
    inputStr = file.read()

c = Circuit()

# added for part 2
c.values['b'] = 956 # 956 is the answer to part 1

c.parseInstructions(inputStr)

print(c.getValue('a'))

# result
"""d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456"""

# https://wiki.python.org/moin/BitwiseOperators

# for NOT : use x^65535 (x XOR 65535)