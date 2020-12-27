import re
from PIL import Image
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
CLAY = re.compile(r"#+")


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


def draw_grid(grid: dict):
    min_x, max_x, min_y, max_y = find_min_max_coordinates(grid)
    case_width = 1
    imgFile = Image.new(
        "RGB",
        (case_width * (1 + max_x - min_x), case_width * (1 + max_y - min_y)),
        (200, 200, 200),
    )
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if grid[x, y] != ".":
                color = (0, 0, 0)
                if grid[x, y] == "~":
                    color = (0, 170, 249)
                elif grid[x, y] == "|":
                    color = (0, 187, 249)
                imgFile.putpixel(((x - min_x) * case_width, y * case_width), color)
    imgFile.show()


def grid_row(y: int, grid: dict, min_x: int, max_x: int):
    return "".join(grid(x, y) for x in range(min_x, max_x + 1))


def evolve_grid(grid: dict, source_x: int, source_y: int):
    x = source_x
    y = source_y
    min_x, max_x, min_y, max_y = find_min_max_coordinates(grid)
    while grid[x, y] != "#":  # go down looking for clay
        grid[x, y] = "|"
        y += 1
        if y > max_y:
            return
    # clay is found, analyze if it is a bassine
    clay_left = min(
        clay_x
        for clay_x, clay_y in grid
        if (clay_y == y and grid[clay_x, clay_y] == "#")
    )
    clay_right = max(
        clay_x
        for clay_x, clay_y in grid
        if (clay_y == y and grid[clay_x, clay_y] == "#")
    )
    fill_y = y - 1
    while grid[clay_left, fill_y] == "#" and grid[clay_right, fill_y] == "#":
        for fill_x in range(clay_left, clay_right + 1):
            if grid[fill_x, fill_y] in ("|", "."):
                grid[fill_x, fill_y] = "~"
        fill_y -= 1


grid = parse_input(example_input)
debug_grid(grid)
evolve_grid(grid, 500, 0)
debug_grid(grid)
evolve_grid(grid, 502, 2)
debug_grid(grid)

grid = parse_input(raw_input)
evolve_grid(grid, 500, 0)
draw_grid(grid)