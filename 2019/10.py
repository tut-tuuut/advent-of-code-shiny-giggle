from collections import namedtuple
import networkx as nx

Asteroid = namedtuple('Point', 'x y')

class AsteroidField:
    def __init__(self, strMap):
        self.graph = nx.Graph()
        self.asteroids = self.parseMap(strMap)
        
    def parseMap(self, strMap):
        rows = strMap.split('\n')
        asteroids = []
        for y,row in enumerate(rows):
            for x,val in enumerate(list(row)):
                if val == '#':
                    a = Asteroid(x,y)
                    asteroids.append(a)
                    self.graph.add_node(a)
        return set(asteroids)

astMap = """.#..#
.....
#####
....#
...##"""
field = AsteroidField(astMap)
print(field.asteroids)
print(field.graph.number_of_nodes())