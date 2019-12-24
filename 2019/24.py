import itertools as it

myInput = """....#
#..#.
##..#
#.###
.####"""

exampleInput = """....#
#..#.
#..##
..#..
#...."""

def nextGrid(grid):
    newGrid = list(map(lambda row: row.copy(), grid)) # grid.copy() is not enough
    for i,j in it.product(range(5), repeat=2):
        adjacentBugs = 0
        if i >= 1:
            adjacentBugs += grid[i-1][j]
        if i <= 3:
            adjacentBugs += grid[i+1][j]
        if j >= 1:
            adjacentBugs += grid[i][j-1]
        if j <= 3:
            adjacentBugs += grid[i][j+1]
        if grid[i][j] == 1 and adjacentBugs != 1:
            newGrid[i][j] = 0
        if grid[i][j] == 0 and adjacentBugs in (1,2):
            newGrid[i][j] = 1
    return newGrid

def printGrid(intGrid):
    for listRow in intGrid:
        print(''.join(list(map(str, listRow))).replace('1','#').replace('0','.'))
    print('\n\n')

strGrid = exampleInput.replace('.','0').replace('#','1')
intGrid = list(map(lambda strRow: list(map(int,list(strRow))),strGrid.split('\n')))
printGrid(intGrid)
nextGr = nextGrid(intGrid)
printGrid(nextGr)
nextGr = nextGrid(nextGr)
printGrid(nextGr)
nextGr = nextGrid(nextGr)
printGrid(nextGr)
nextGr = nextGrid(nextGr)
printGrid(nextGr)