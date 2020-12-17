from collections import defaultdict
from itertools import product
from operator import itemgetter

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """
.#.
..#
###
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def build_grid_from_input(input):
    """return a defaultdict() with (x,y,z) coordinates as keys and 1 as values for active cubes"""
    rows = input.strip().splitlines()
    grid = defaultdict(int)  # grid[something] will be 0 if <something> is not defined
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == "#":
                grid[x, y, 0] = 1
    return grid


def get_bounds(grid):
    """Return coordinates of the two opposite corners of the area containing all active cubes"""
    max_point = (max(grid, key=itemgetter(i))[i] for i in range(3))
    min_point = (min(grid, key=itemgetter(i))[i] for i in range(3))
    return (*min_point, *max_point)


def build_new_grid(grid):
    """return the next state of grid, given the current one"""
    new_grid = defaultdict(int)
    low_x, low_y, low_z, top_x, top_y, top_z = get_bounds(grid)
    for x, y, z in product(
        range(low_x - 1, top_x + 2),  # expand the exploration from 1 cube
        range(low_y - 1, top_y + 2),
        range(low_z - 1, top_z + 2),
    ):
        if grid[x, y, z] == 1:
            if count_active_neighbors(grid, x, y, z) in (2, 3):
                new_grid[x, y, z] = 1
        else:
            if count_active_neighbors(grid, x, y, z) == 3:
                new_grid[x, y, z] = 1
    return new_grid


def count_active_neighbors(grid, *coordinates):
    x, y, z = coordinates
    return -grid[x, y, z] + sum(
        grid[xn, yn, zn]
        for xn in range(x - 1, x + 2)
        for yn in range(y - 1, y + 2)
        for zn in range(z - 1, z + 2)
    )


def boot_grid_for_6_cycles(raw_input):
    grid = build_grid_from_input(raw_input)
    for i in range(6):
        grid = build_new_grid(grid)
    return sum(grid.values())


u.assert_equals(boot_grid_for_6_cycles(example_input), 112)

u.answer_part_1(boot_grid_for_6_cycles(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# Basically the same as part 1, with 4 dimensions:
# I copy-pasted and added "hyper" in function names.


def build_hyper_grid_from_input(input):
    rows = input.strip().splitlines()
    grid = defaultdict(int)  # grid[something] will be 0 if <something> is not defined
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == "#":
                grid[x, y, 0, 0] = 1
    return grid


def get_hyper_bounds(grid):
    max_point = (max(grid, key=itemgetter(i))[i] for i in range(4))
    min_point = (min(grid, key=itemgetter(i))[i] for i in range(4))
    return (*min_point, *max_point)


def build_new_hyper_grid(grid):
    new_grid = defaultdict(int)
    low_x, low_y, low_z, low_w, top_x, top_y, top_z, top_w = get_hyper_bounds(grid)
    for x, y, z, w in product(
        range(low_x - 1, top_x + 2),
        range(low_y - 1, top_y + 2),
        range(low_z - 1, top_z + 2),
        range(low_w - 1, top_w + 2),
    ):
        if grid[x, y, z, w] == 1:
            if count_active_hyper_neighbors(grid, x, y, z, w) in (2, 3):
                new_grid[x, y, z, w] = 1
        else:
            if count_active_hyper_neighbors(grid, x, y, z, w) == 3:
                new_grid[x, y, z, w] = 1
    return new_grid


def count_active_hyper_neighbors(grid, *coordinates):
    x, y, z, w = coordinates
    return -grid[x, y, z, w] + sum(
        grid[xn, yn, zn, wn]
        for xn in range(x - 1, x + 2)
        for yn in range(y - 1, y + 2)
        for zn in range(z - 1, z + 2)
        for wn in range(w - 1, w + 2)
    )


def boot_hyper_grid_for_6_cycles(raw_input):
    grid = build_hyper_grid_from_input(raw_input)
    for i in range(6):
        # print(f"{i} - {sum(grid.values())}")
        grid = build_new_hyper_grid(grid)
    return sum(grid.values())


u.assert_equals(boot_hyper_grid_for_6_cycles(example_input), 848)

u.answer_part_1(boot_hyper_grid_for_6_cycles(raw_input))
