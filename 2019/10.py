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
        for i,a in enumerate(self.asteroids):
            print(f'parsing lines of view {int(100*i/len(self.asteroids))}%...', end='\r')
            for b in self.asteroids:
                if a == b:
                    continue
                if self.do_they_see_each_other(a,b):
                    self.graph.add_edge(a.coord,b.coord)
        print('done!')
    
    def pente(self, a):
        # get inclination of a given segment
        s = self.station
        if s.x == a.x:
            return float('inf')
        return (a.y - s.y)/(a.x - s.x)
    
    def vaporise_asteroids(self):
        print('yayyyy! destrooooy!')
        detectables = list(filter(lambda x: self.do_they_see_each_other(self.station,x), self.asteroids))
        detectables.remove(self.station)
        print(f'{len(detectables)} asteroids detectable')
        # divide
        left = list(filter(lambda a: a.x < self.station.x, detectables))
        print(f'{len(left)} asteroids on the left half of the screen')
        # sort the asteroids on the left
        left = sorted(left, key=self.pente)
        print(left[0:5])
        firstOnTheLeft = len(detectables) - len(left) + 1
        bet = left[200 - firstOnTheLeft]
        print(f'answer to part2: {100*bet.x + bet.y}')


astMap = """..#..###....#####....###........#
.##.##...#.#.......#......##....#
#..#..##.#..###...##....#......##
..####...#..##...####.#.......#.#
...#.#.....##...#.####.#.###.#..#
#..#..##.#.#.####.#.###.#.##.....
#.##...##.....##.#......#.....##.
.#..##.##.#..#....#...#...#...##.
.#..#.....###.#..##.###.##.......
.##...#..#####.#.#......####.....
..##.#.#.#.###..#...#.#..##.#....
.....#....#....##.####....#......
.#..##.#.........#..#......###..#
#.##....#.#..#.#....#.###...#....
.##...##..#.#.#...###..#.#.#..###
.#..##..##...##...#.#.#...#..#.#.
.#..#..##.##...###.##.#......#...
...#.....###.....#....#..#....#..
.#...###..#......#.##.#...#.####.
....#.##...##.#...#........#.#...
..#.##....#..#.......##.##.....#.
.#.#....###.#.#.#.#.#............
#....####.##....#..###.##.#.#..#.
......##....#.#.#...#...#..#.....
...#.#..####.##.#.........###..##
.......#....#.##.......#.#.###...
...#..#.#.........#...###......#.
.#.##.#.#.#.#........#.#.##..#...
.......#.##.#...........#..#.#...
.####....##..#..##.#.##.##..##...
.#.#..###.#..#...#....#.###.#..#.
............#...#...#.......#.#..
.........###.#.....#..##..#.##..."""
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

field.vaporise_asteroids()