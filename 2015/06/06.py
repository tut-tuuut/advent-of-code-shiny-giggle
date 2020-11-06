grid = []
size = 10

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
    
    def countLights(self):
        return sum(map(sum, self.grid))
    
    def debug(self):
        for x in range(size):
            print(self.grid[x])
        print('-'*2*size)

grid = Grid(size)
grid.turnOn(2,2,5,5)
grid.debug()

grid.turnOff(3,4,5,5)
grid.debug()

grid.toggle(2,2,4,4)
grid.debug()
print(grid.countLights())
