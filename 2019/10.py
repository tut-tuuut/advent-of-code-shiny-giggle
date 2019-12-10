from collections import namedtuple
import networkx as nx

Asteroid = namedtuple('Point', 'x y coord')

class AsteroidField:
    def __init__(self, strMap):
        self.graph = nx.Graph()
        self.asteroids = self.parseMap(strMap)
        print(f'{len(self.asteroids)} asteroids in this field...')
        self.parseLinesOfView()
        
    def parseMap(self, strMap):
        rows = strMap.split('\n')
        asteroids = []
        for y,row in enumerate(rows):
            for x,val in enumerate(list(row)):
                if val == '#':
                    a = Asteroid(x,y,f'{x}•{y}')
                    asteroids.append(a)
                    self.graph.add_node(a.coord)
        return set(asteroids)
    
    def do_they_see_each_other(self,a,b):
        if b in self.graph.adj[a.coord]:
            return True
        if (abs(a.x - b.x)) == 1 or (abs(a.y - b.y)) == 1:
            return True
        for c in self.asteroids:
            if a == c or b == c:
                continue
            if not(min(a.x,b.x) <= c.x <= max(b.x,a.x)):
                continue
            if not(min(a.y,b.y) <= c.y <= max(b.y,a.y)):
                continue
            if (b.x-a.x)*(c.y-a.y) == (b.y-a.y)*(c.x-a.x): #xy' - yx' = 0
                return False
        return True

    def parseLinesOfView(self):
        for a in self.asteroids:
            for b in self.asteroids:
                if a == b:
                    continue
                if self.do_they_see_each_other(a,b):
                    self.graph.add_edge(a.coord,b.coord)

astMap = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##"""
field = AsteroidField(astMap)

maxDetected = 0
for ast in field.asteroids:
    neighbours = list(field.graph.neighbors(ast.coord))
    if len(neighbours) > maxDetected:
        bestLocation = ast
        maxDetected = len(neighbours)
print(f'best location is {bestLocation.coord}')
print(f'you can detect {maxDetected} asteroids from there!')