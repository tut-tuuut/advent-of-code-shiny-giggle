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
    print(f"┌{'─'*len(grid[0])}┐")
    for row in grid:
        print("│" + "".join(u.yellow("◼︎", True) if val else " " for val in row) + "│")
    print(f"└{'─'*len(grid[0])}┘")


def construct_grid(raw_input):
    is_dot = re.compile(r"(\d+),(\d+)")
    is_fold = re.compile(r"fold along ([xy])=(\d+)")
    dots = [(int(x), int(y)) for x, y in re.findall(is_dot, example)]
    folds = [(axis, int(coord)) for axis, coord in re.findall(is_fold, example)]
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
    if axis == "y":  # horizontal fold
        if value != (len(grid) - 1) / 2:
            return
        new_grid = [
            [(grid[y][x] or grid[len(grid) - 1 - y][x]) for x in range(len(grid[0]))]
            for y in range(int((len(grid) - 1) / 2))
        ]
    return new_grid


grid, folds = construct_grid(raw_input)
new_grid = fold_grid(grid, folds[0])
debug_grid(new_grid)
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
