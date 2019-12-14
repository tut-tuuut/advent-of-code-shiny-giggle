from collections import namedtuple
Chemical = namedtuple('Chemical', 'qty name')
Reaction = namedtuple('Reaction', 'input output')

def chemical_from_string(string):
    strqty, name = string.strip().split(' ')
    return Chemical(int(strqty), name)

class Nanofactory:
    def parseRecipes(self, string):
        self.recipes = {}
        rows = string.split('\n')
        for row in rows:
            strReactives, strProduct = row.split(' => ')
            inputs = tuple(map(chemical_from_string, strReactives.split(', ')))
            output = chemical_from_string(strProduct)
            self.recipes[output.name] = Reaction(inputs, output)

f = Nanofactory()
with open(__file__ + '.t1-165') as file:
    string = file.read()

f.parseRecipes(string)