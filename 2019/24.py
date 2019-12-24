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

def nextGrid(strGrid):
    strGrid = strGrid.replace('.','0').replace('#','1')
    grid = list(map(list,strGrid.split('\n')))
    newGrid = grid.copy()
    for i,j in it.product(range(5), repeat=2):
        print(f'{i} {j} {grid[i][j]}')

nextGrid(exampleInput)