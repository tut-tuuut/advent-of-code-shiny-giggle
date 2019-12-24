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

exampleInput = """.....
.....
.....
#....
.#..."""

def deepCopy(grid):
    return list(map(lambda row: row.copy(), grid)) # grid.copy() is not enough

def nextGrid(grid, depth):
    grid = deepCopy(grid)
    grid[2][2] = 0
    newGrid = deepCopy(grid)
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
        if i == 0:
            print('add top-level grid[1][2] to adjacent bugs')
        elif i == 4:
            print('add top-evel grid[3][2] to adjacent bugs')
        if j == 0:
            print('add top-level grid[2][1] to adjacent bugs')
        elif j == 4:
            print('add top-level grid[2][3] to adjacent bugs')
        if i == 2 and j == 1:
            print('add left-column of sublevel grid to adjacent bugs')
        elif i == 2 and j == 3:
            print('add right-column of sublevel grid to adjacent bugs')
        elif i == 1 and j == 2:
            print('add top-row of sublevel grid to adjacent bugs')
        elif i == 3 and j == 2:
            print('add bottom-row of sublevel grid to adjacent bugs')
        if grid[i][j] == 1 and adjacentBugs != 1:
            newGrid[i][j] = 0
        if grid[i][j] == 0 and adjacentBugs in (1,2):
            newGrid[i][j] = 1
    newGrid[2][2] = 0
    return newGrid

def bugCount(intGrid):
    return sum(list(map(sum, intGrid)))

def column(intGrid, index):
    return list(map(lambda row: row[index], intGrid))

def printGrid(intGrid):
    intGrid = deepCopy(intGrid)
    intGrid[2][2] = 2
    for listRow in intGrid:
        print(''.join(list(map(str, listRow))).replace('1','#').replace('0','.').replace('2', '?'))
    print('\n\n')

        

strGrid = myInput.replace('.','0').replace('#','1')
intGrid = list(map(lambda strRow: list(map(int,list(strRow))),strGrid.split('\n')))
print(intGrid)
printGrid(intGrid)
print(column(intGrid, 0))
print(column(intGrid, 4))