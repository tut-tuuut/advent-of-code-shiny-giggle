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
        self.quantities[name] -= qty
    def make(self, qty, name, level):
        if (name == 'ORE'):
            self.exctractedOre += qty
            return
        if (self.quantities[name] >= qty):
            return
        reaction = self.recipes[name]
        neededToProduce = qty - self.quantities[name]
        multiplier = math.ceil(neededToProduce / reaction.output.qty)
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

f = Nanofactory()
with open(__file__ + '.t2-13312') as file:
    string2 = file.read()
f.parseRecipes(string2)
f.make(1, 'FUEL', 0)
print(f'this should be 13312: {f.exctractedOre}')

print('REAL INPUT ---!')
f = Nanofactory()
with open(__file__ + '.input') as file:
    string2 = file.read()
f.parseRecipes(string2)
f.make(1, 'FUEL', 0)
print(f'this should be more than 260483 and less than 453838: {f.exctractedOre}')

f = Nanofactory()
with open(__file__ + '.t2-13312') as file:
    string2 = file.read()
f.parseRecipes(string2)
f.make(1, 'FUEL', 0)
oreForOneFuel = f.exctractedOre
fuelqty = 1
oreReserve = 1000000000000
minimumFeasibleFuel = int(oreReserve/oreForOneFuel)
f.make(minimumFeasibleFuel, 'FUEL', 0)
f.use(minimumFeasibleFuel, 'FUEL')
fuelqty += minimumFeasibleFuel
print(f'extracted {f.exctractedOre} to produce {fuelqty}')
while oreReserve > f.exctractedOre:
    percentage = int(100*f.exctractedOre/oreReserve)
    if percentage < 97:
        fueltomake = 320
    elif percentage < 99:
        fueltomake = 200
    else:
        fueltomake = 1
    f.make(fueltomake, 'FUEL', 0)
    f.use(fueltomake, 'FUEL')
    fuelqty += fueltomake
    print(f'fuel qty : {fuelqty} extracted ore: {f.exctractedOre} ({percentage}%)', end='\r')
print('')
print(f'this should be 82892753: {fuelqty}')