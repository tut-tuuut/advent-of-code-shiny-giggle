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
    return list(map(lambda row: row.copy(), grid))  # grid.copy() is not enough


def nextGrid(grid):
    newGrid = deepCopy(grid)
    for i, j in it.product(range(5), repeat=2):
        adjacentBugs = 0
        if i >= 1:
            adjacentBugs += grid[i - 1][j]
        if i <= 3:
            adjacentBugs += grid[i + 1][j]
        if j >= 1:
            adjacentBugs += grid[i][j - 1]
        if j <= 3:
            adjacentBugs += grid[i][j + 1]
        if grid[i][j] == 1 and adjacentBugs != 1:
            newGrid[i][j] = 0
        if grid[i][j] == 0 and adjacentBugs in (1, 2):
            newGrid[i][j] = 1
    return newGrid


def printGrid(intGrid):
    for listRow in intGrid:
        print("".join(list(map(str, listRow))).replace("1", "#").replace("0", "."))
    print("\n\n")


def diversityRating(intGrid):
    grid = deepCopy(intGrid)
    for row in grid:
        row.reverse()
    number = list(map(lambda row: "".join(list(map(str, row))), grid))
    number.reverse()
    return int("".join(number), 2)


strGrid = myInput.replace(".", "0").replace("#", "1")
intGrid = list(map(lambda strRow: list(map(int, list(strRow))), strGrid.split("\n")))

grids = []
grids.append(deepCopy(intGrid))

for i in it.count():
    print(f"looking for repeating patterns round {i}", end="\r")
    newGrid = nextGrid(intGrid)
    if newGrid in grids:
        print(f"\npart1: biodiversity rating is {diversityRating(newGrid)}")
        break
    grids.append(deepCopy(newGrid))
    intGrid = newGrid
