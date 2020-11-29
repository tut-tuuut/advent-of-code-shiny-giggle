import utils as u


def build_grid_from_string(string):
    return [
        [1 if char == "#" else 0 for char in stringRow]
        for stringRow in string.split("\n")
        if stringRow != ""
    ]


def count_neighbors(i, j, grid):
    return -grid[i][j] + sum(
        grid[row][column]
        for row in range(i - 1, i + 2)
        for column in range(j - 1, j + 2)
        if row >= 0 and row < len(grid) and column >= 0 and column < len(grid[i])
    )


def debug_bordel(i, j, grid):
    for row in range(i - 1, i + 2):
        for column in range(j - 1, j + 2):
            if (
                row > 0
                and row < len(grid) - 1
                and column > 0
                and column < len(grid[i]) - 1
            ):
                print(f"row {row} column {column}")


exampleStr = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

grid = build_grid_from_string(exampleStr)

u.assert_equals(count_neighbors(5, 5, grid), 1)
u.assert_equals(count_neighbors(0, 5, grid), 1)
u.assert_equals(count_neighbors(0, 0, grid), 1)
u.assert_equals(count_neighbors(0, 0, grid), 1)
u.assert_equals(count_neighbors(4, 1, grid), 6)

debug_bordel(0, 0, grid)

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()
