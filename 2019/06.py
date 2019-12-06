class SpaceObject:
    space = {} # spaaaace
    def __init__(self, name):
        self.name = name
        self.space[name] = self
        self.parent = None

    def setParent(self, parent):
        self.parent = parent

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

example = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

l = list(map(lambda s: tuple(s.split(')')), example.split('\n')))
for couple in l:
    o = SpaceObject(couple[1])
    o = SpaceObject(couple[0])
for couple in l:
    center,orbit = couple
    SpaceObject.find(orbit).setParent(SpaceObject.find(center))
for o in SpaceObject.all():
    o.debug()
