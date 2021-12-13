import utils as u
import re
import itertools

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def debug_grid(grid):
    print(f"┌─{'─'*len(grid[0])}┐")
    for row in grid:
        print("│ " + "".join("█" if val else " " for val in row) + "│")
    print(f"└─{'─'*len(grid[0])}┘")


def construct_grid(raw_input):
    is_dot = re.compile(r"(\d+),(\d+)")
    is_fold = re.compile(r"fold along ([xy])=(\d+)")
    dots = [(int(x), int(y)) for x, y in re.findall(is_dot, raw_input)]
    folds = [(axis, int(coord)) for axis, coord in re.findall(is_fold, raw_input)]
    max_x_dot = max(x for x, _ in dots)
    max_y_dot = max(y for _, y in dots)
    max_x_fold = max(val for axis, val in folds if axis == "x")
    max_y_fold = max(val for axis, val in folds if axis == "y")
    max_x = 1 + max(max_x_dot, 2 * max_x_fold)
    max_y = 1 + max(max_y_dot, 2 * max_y_fold)
    grid = [[False for _ in range(max_x)] for _ in range(max_y)]
    for x, y in dots:
        grid[y][x] = True
    return grid, folds


def fold_grid(grid, fold):
    axis, value = fold
    width = len(grid[0])
    height = len(grid)
    if axis == "y":  # horizontal fold
        if value != (height - 1) / 2:
            return
        new_grid = [
            [(grid[y][x] or grid[height - 1 - y][x]) for x in range(width)]
            for y in range(int((height - 1) / 2))
        ]
    elif axis == "x":  # vertical fold
        if value != ((width - 1) / 2):
            return
        new_grid = [
            [(row[x] or row[width - 1 - x]) for x in range(int((width - 1) / 2))]
            for row in grid
        ]
    return new_grid


grid, folds = construct_grid(example)
new_grid = fold_grid(grid, folds[0])
new_grid = fold_grid(new_grid, folds[1])

grid, folds = construct_grid(raw_input)
new_grid = fold_grid(grid, folds.pop(0))
u.answer_part_1(sum(sum(1 if val else 0 for val in row) for row in new_grid))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

for fold in folds:
    new_grid = fold_grid(new_grid, fold)

u.answer_part_2("RCPLAKHL")
debug_grid(new_grid)
