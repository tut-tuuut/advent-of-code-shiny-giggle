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

emptyGrid = """.....
.....
.....
.....
....."""


def deepCopy(grid):
    return list(map(lambda row: row.copy(), grid))  # grid.copy() is not enough


def column(intGrid, index):
    return list(map(lambda row: row[index], intGrid))


class Eris:
    def __init__(self):
        self.grids = {}

    def value(self, i, j, depth):
        if depth not in self.grids.keys():
            return 0
        else:
            return self.grids[depth][i][j]

    def grid(self, depth):
        if depth not in self.grids.keys():
            return parseStrGrid(emptyGrid)
        else:
            return self.grids[depth]

    def nextGrid(self, depth):
        grid = deepCopy(self.grids[depth])
        grid[2][2] = 0
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
            if i == 0:
                adjacentBugs += self.value(1, 2, depth - 1)
            elif i == 4:
                adjacentBugs += self.value(3, 2, depth - 1)
            if j == 0:
                adjacentBugs += self.value(2, 1, depth - 1)
            elif j == 4:
                adjacentBugs += self.value(2, 3, depth - 1)
            if i == 2 and j == 1:
                adjacentBugs += sum(column(self.grid(depth + 1), 0))
                # add left-column of sublevel grid to adjacent bugs
            elif i == 2 and j == 3:
                adjacentBugs += sum(column(self.grid(depth + 1), 4))
                # add right-column of sublevel grid to adjacent bugs
            elif i == 1 and j == 2:
                adjacentBugs += sum(self.grid(depth + 1)[0])
                # add top-row of sublevel grid to adjacent bugs
            elif i == 3 and j == 2:
                adjacentBugs += sum(self.grid(depth + 1)[4])
                # add bottom-row of sublevel grid to adjacent bugs
            if grid[i][j] == 1 and adjacentBugs != 1:
                newGrid[i][j] = 0
            if grid[i][j] == 0 and adjacentBugs in (1, 2):
                newGrid[i][j] = 1
        newGrid[2][2] = 0
        return newGrid


def bugCount(intGrid):
    return sum(list(map(sum, intGrid)))


def printGrid(intGrid):
    intGrid = deepCopy(intGrid)
    intGrid[2][2] = 2
    for listRow in intGrid:
        print(
            "".join(list(map(str, listRow)))
            .replace("1", "#")
            .replace("0", ".")
            .replace("2", "?")
        )
    print("\n\n")


def parseStrGrid(strGrid):
    strGrid = strGrid.replace(".", "0").replace("#", "1").replace("?", "0")
    return list(map(lambda strRow: list(map(int, list(strRow))), strGrid.split("\n")))


eris = Eris()
eris.grids[0] = parseStrGrid(myInput)

for minute in range(1, 201):
    eris.grids[-minute] = parseStrGrid(emptyGrid)
    eris.grids[minute] = parseStrGrid(emptyGrid)
    newGrids = {}
    for depth in eris.grids.keys():
        newGrids[depth] = eris.nextGrid(depth)
    eris.grids = newGrids

totalBugs = 0
for depth in eris.grids.keys():
    bugs = bugCount(eris.grid(depth))
    totalBugs += bugs
print(f"{totalBugs} total")
