import re

grid = []
size = 1000

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [ [0]*size for e in range(size) ]
        print(f'Initiated a {size}*{size} grid.')
    
    def turnOn(self, xstart, ystart, xend, yend):
        for x in range(xstart, xend+1):
            for y in range(ystart, yend+1):
                self.grid[x][y] = 1
    
    def turnOff(self, xstart, ystart, xend, yend):
        for x in range(xstart, xend+1):
            for y in range(ystart, yend+1):
                self.grid[x][y] = 0
    
    def toggle(self, xstart, ystart, xend, yend):
        for x in range(xstart, xend+1):
            for y in range(ystart, yend+1):
                self.grid[x][y] = 1 - self.grid[x][y]
    
    def processInstruction(self, instruction):
        print(f'process instruction "{instruction}"')
        coordinates = re.findall(r'(\d+),(\d+) through (\d+),(\d+)', instruction)[0]
        xstart, ystart, xend, yend = map(int, coordinates)
        if (instruction[1] == 'o'): #t*o*ggle
            return self.toggle(xstart, ystart, xend, yend)
        if (instruction[6] == 'f'): #turn o*f*f
            return self.turnOff(xstart, ystart, xend, yend)
        if (instruction[6] == 'n'): #turn o*n*
            return self.turnOn(xstart, ystart, xend, yend)
    
    def countLights(self):
        return sum(map(sum, self.grid))
    
    def debug(self):
        for x in range(size):
            print(self.grid[x])
        print('-'*2*size)





class GridTwo(Grid):
    def turnOn(self, xstart, ystart, xend, yend):
        for x in range(xstart, xend+1):
            for y in range(ystart, yend+1):
                self.grid[x][y] += 1
    
    def turnOff(self, xstart, ystart, xend, yend):
        for x in range(xstart, xend+1):
            for y in range(ystart, yend+1):
                self.grid[x][y] = max(self.grid[x][y] - 1, 0)
    
    def toggle(self, xstart, ystart, xend, yend):
        for x in range(xstart, xend+1):
            for y in range(ystart, yend+1):
                self.grid[x][y] = 2 + self.grid[x][y]

grid = Grid(size)
grid2 = GridTwo(size)

with open(__file__+'.input', "r+") as file:
    inputStr = file.read()

for instruction in filter(None, inputStr.split('\n')):
    grid.processInstruction(instruction)
    grid2.processInstruction(instruction)

print(f'PART1 : {grid.countLights()}')
print(f'PART2 : {grid2.countLights()}')