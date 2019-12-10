from collections import namedtuple
import networkx as nx

Asteroid = namedtuple('Point', 'x y')

class AsteroidField:
    def __init__(self, strMap):
        self.graph = nx.Graph()
        self.asteroids = self.parseMap(strMap)
        self.parseLinesOfView()
        
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
    
    def do_they_see_each_other(self,a,b):
        if b in self.graph.adj[a]:
            return True
        if (abs(a.x - b.x)) == 1 or (abs(a.y - b.y)) == 1:
            return True
        for c in self.asteroids:
            if a == c or b == c:
                continue
            if not(a.x <= c.x <= b.x) or not(a.y <= c.y <= b.y):
                continue
            if b.x == a.x:
                if a.y < c.y < b.y:
                    return False
                continue
            alpha = 1.0 * (b.y - a.y) / (b.x - a.x)
            if c.y == c.x * alpha + a.y - a.x * alpha:
                return False
        return True

    def parseLinesOfView(self):
        for a in self.asteroids:
            for b in self.asteroids:
                if a == b:
                    continue
                if self.do_they_see_each_other(a,b):
                    self.graph.add_edge(a,b)

astMap = """.#..#
.....
#####
....#
...##"""
field = AsteroidField(astMap)
print(field.asteroids)
print(field.graph.number_of_nodes())