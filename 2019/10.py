from collections import namedtuple
import networkx as nx

Asteroid = namedtuple('Point', 'x y coord')

class AsteroidField:
    def __init__(self, strMap):
        self.graph = nx.Graph()
        self.asteroids = self.parseMap(strMap)
        print(f'{len(self.asteroids)} asteroids in this {self.width}x{self.height} field...')
        self.parseLinesOfView()
    
    def setStation(self, asteroid):
        self.station = asteroid
        
    def parseMap(self, strMap):
        rows = strMap.split('\n')
        asteroids = []
        self.width, self.height = len(rows[0]), len(rows)
        for y,row in enumerate(rows):
            for x,val in enumerate(list(row)):
                if val == '#':
                    a = Asteroid(x,y,f'{x}•{y}')
                    asteroids.append(a)
                    self.graph.add_node(a.coord)
        return list(asteroids)
    
    def is_c_between_a_and_b(self,a,b,c):
        if not(min(a.x,b.x) <= c.x <= max(b.x,a.x)):
            return False
        if not(min(a.y,b.y) <= c.y <= max(b.y,a.y)):
            return False
        if (b.x-a.x)*(c.y-a.y) == (b.y-a.y)*(c.x-a.x): #xy' - yx' = 0
            return True
        return False
    
    def do_they_see_each_other(self,a,b):
        if b in self.graph.adj[a.coord]:
            return True
        if (abs(a.x - b.x)) == 1 or (abs(a.y - b.y)) == 1:
            return True
        for c in self.asteroids:
            if a == c or b == c:
                continue
            if self.is_c_between_a_and_b(a,b,c):
                return False
        return True

    def parseLinesOfView(self):
        for a in self.asteroids:
            for b in self.asteroids:
                if a == b:
                    continue
                if self.do_they_see_each_other(a,b):
                    self.graph.add_edge(a.coord,b.coord)
    
    def rotate_station(self):
        #target bounds
        minx = -1*self.station.x
        miny = -1*self.station.y
        maxx = 2*self.width - self.station.x
        maxy = 2*self.height - self.station.y

        target = [self.station.x, miny]
        while True:
            while target[0] < maxx:
                target[0] += 1
                yield target
            while target[1] < maxy:
                target[1] += 1
                yield target
            while target[0] > minx:
                target[0] -= 1
                yield target
            while target[1] > miny:
                target[1] -= 1
                yield target
    
    def vaporise_asteroids(self):
        print('kabooom!')









astMap = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
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

field.setStation(bestLocation)

for i,target in enumerate(field.rotate_station()):
    print(target)
    if i > 100:
        break