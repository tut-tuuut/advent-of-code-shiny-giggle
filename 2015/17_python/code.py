import re
from collections import defaultdict

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

with open(__file__ + ".example.txt", "r+") as file:
    example_input = file.read()

# Part 1

# x=504, y=10..13
# y=13, x=498..504
ROW = re.compile(r"(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)")


def parse_input(input: str):
    grid = defaultdict(lambda: ".")
    for r in input.splitlines():
        fixed, fixed_val, _, variable_min, variable_max = ROW.search(r).groups()
        if fixed == "x":
            x = int(fixed_val)
            for y in range(int(variable_min), int(variable_max) + 1):
                grid[x, y] = "#"
        elif fixed == "y":
            y = int(fixed_val)
            for x in range(int(variable_min), int(variable_max) + 1):
                grid[x, y] = "#"
    return grid


def find_min_max_coordinates(grid: dict):
    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)
    return (min_x, max_x, 0, max_y)


def debug_grid(grid: dict):
    min_x, max_x, min_y, max_y = find_min_max_coordinates(grid)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if x == 500 and y == 0:
                print("+", end="")
                continue
            print(grid[x, y], end="")
        print("")


grid = parse_input(example_input)
debug_grid(grid)
