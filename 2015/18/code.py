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


def build_next_grid(grid):
    newGrid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            lit_neighbors = count_neighbors(i, j, grid)
            if lit_neighbors == 3:
                row.append(1)
            elif lit_neighbors == 2:
                row.append(grid[i][j])
            else:
                row.append(0)
        newGrid.append(row)
    return newGrid


def turn_corners_on(grid):
    grid[0][0] = 1
    grid[0][len(grid) - 1] = 1
    grid[len(grid) - 1][0] = 1
    grid[len(grid) - 1][len(grid) - 1] = 1


def build_next_grid_with_four_corners_on(grid):
    newGrid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            lit_neighbors = count_neighbors(i, j, grid)
            if lit_neighbors == 3:
                row.append(1)
            elif lit_neighbors == 2:
                row.append(grid[i][j])
            else:
                row.append(0)
        newGrid.append(row)
    turn_corners_on(newGrid)
    return newGrid


def count_lights_on(grid):
    return sum([sum(row) for row in grid])


def debug_grid(grid):
    print(
        "\n".join(
            map(
                lambda row: "".join(map(lambda value: "#" if value == 1 else ".", row)),
                grid,
            )
        )
    )
    print("--------")


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

for _ in range(4):
    grid = build_next_grid(grid)

u.assert_equals(count_lights_on(grid), 4)

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()

grid = build_grid_from_string(inputStr)

for _ in range(100):
    grid = build_next_grid(grid)

u.answer_part_1(count_lights_on(grid))

# --- part 2 ------

grid = build_grid_from_string(exampleStr)
turn_corners_on(grid)

for _ in range(5):
    grid = build_next_grid_with_four_corners_on(grid)

u.assert_equals(count_lights_on(grid), 17)

grid = build_grid_from_string(inputStr)
turn_corners_on(grid)

for _ in range(100):
    grid = build_next_grid_with_four_corners_on(grid)

u.answer_part_2(count_lights_on(grid))
