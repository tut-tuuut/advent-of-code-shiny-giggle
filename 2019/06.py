class SpaceObject:
    space = {} # spaaaace
    def __init__(self, name):
        self.name = name
        self.space[name] = self
        self.parent = None

    def setParent(self, parent):
        self.parent = parent

    def orbitCount(self):
        if self.parent == None:
            return 0
        else:
            return 1 + self.parent.orbitCount()

    def debug(self):
        print(f'I am {self.name}')
        if self.parent == None:
            print('I AM THE CENTER OF MASS')
        else:
            print(f'I orbit around {self.parent.name}')

    @classmethod
    def find(cls, objname):
        return cls.space[objname]
    
    @classmethod
    def all(cls):
        return list(map(cls.find, cls.space))

with open(__file__ + '.input') as file:
    input = file.read()

l = list(map(lambda s: tuple(s.split(')')), input.split('\n')))
for couple in l: # I will instantiate most of them twice, but oh well
    o = SpaceObject(couple[1])
    o = SpaceObject(couple[0])
for couple in l: # Each object stores a reference to its parent
    center,orbit = couple
    SpaceObject.find(orbit).setParent(SpaceObject.find(center))

print('1st part:')
print(sum(list(map(lambda o: o.orbitCount(), SpaceObject.all()))))

