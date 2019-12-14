from collections import namedtuple
import math
Chemical = namedtuple('Chemical', 'qty name')
Reaction = namedtuple('Reaction', 'input output')

def chemical_from_string(string):
    strqty, name = string.strip().split(' ')
    return Chemical(int(strqty), name)

class Nanofactory:
    def __init__(self):
        self.quantities = {'ORE':0}
        self.exctractedOre = 0
    def parseRecipes(self, string):
        self.recipes = {}
        rows = string.split('\n')
        for row in rows:
            strReactives, strProduct = row.split(' => ')
            inputs = tuple(map(chemical_from_string, strReactives.split(', ')))
            output = chemical_from_string(strProduct)
            self.recipes[output.name] = Reaction(inputs, output)
            self.quantities[output.name] = 0
    def use(self, qty, name):
        print(f'use {qty} {name}')
        self.quantities[name] -= qty
    def make(self, qty, name, level):
        print(f'{"-"*level} need {qty} {name}')
        if (name == 'ORE'):
            self.exctractedOre += qty
            return
        if (self.quantities[name] >= qty):
            print(f'already have {self.quantities[name]} {name}')
            self.use(qty, name)
            return
        reaction = self.recipes[name]
        neededToProduce = qty - self.quantities[name]
        multiplier = math.ceil(neededToProduce / reaction.output.qty)
        print(f'{"-"*level} have {self.quantities[name]} left')
        print(f'{"-"*level} will produce {multiplier*reaction.output.qty} {name}')
        for reactive in reaction.input:
            self.make(multiplier * reactive.qty, reactive.name, level + 1)
            self.use(multiplier * reactive.qty, reactive.name)
        self.quantities[name] += reaction.output.qty * multiplier
        return

f = Nanofactory()
with open(__file__ + '.t1-31') as file:
    string1 = file.read()

f.parseRecipes(string1)
f.make(1, 'FUEL',0)
print(f'this should be 31: {f.exctractedOre}')

f = Nanofactory()
with open(__file__ + '.t3-165') as file:
    string2 = file.read()

f.parseRecipes(string2)
f.make(1, 'FUEL', 0)
print(f'this should be 165: {f.exctractedOre}') # 260483 too low
print(f.quantities['ORE'])