import re
import itertools
from PIL import Image
from collections import defaultdict, deque

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
            return []
    # clay is found, analyze its width
    try:
        clay_left = 1 + max(
            clay_x for clay_x in range(min_x, x) if grid[clay_x, y] not in ("#", "~")
        )
    except ValueError:
        clay_left = min_x
    try:
        clay_right = -1 + min(
            clay_x
            for clay_x in range(x + 1, max_x + 1)
            if grid[clay_x, y] not in ("#", "~")
        )
    except ValueError:
        clay_right = max_x
    # fill the bassine if there is one
    fill_y = y - 1
    fill_left = clay_left
    fill_right = clay_right
    while grid[fill_left, fill_y] == "#" and grid[fill_right, fill_y] == "#":
        for fill_x in range(fill_left, fill_right + 1):
            if grid[fill_x, fill_y] in ("|", "."):
                grid[fill_x, fill_y] = "~"
        fill_y -= 1  # go up
        # check right side is still clay
        for check_x in range(x, clay_right + 1):
            if grid[check_x, fill_y] == "#":
                fill_right = check_x
                break
        # check left side is still clay
        for check_x in range(x, clay_left - 1, -1):
            if grid[check_x, fill_y] == "#":
                fill_left = check_x
                break
    # flow to left and right
    next_sources = []
    for flow_x in itertools.count(x, 1):  # to the right
        if grid[flow_x, fill_y] == "#":
            break  # stop when meeting clay
        if grid[flow_x, fill_y + 1] not in ("#", "~"):
            grid[flow_x, fill_y] = "|"
            next_sources.append((flow_x, fill_y))
            break
        grid[flow_x, fill_y] = "|"
    for flow_x in itertools.count(x, -1):  # to the left
        if grid[flow_x, fill_y] == "#":
            break  # stop when meeting clay
        if grid[flow_x, fill_y + 1] not in ("#", "~"):
            grid[flow_x, fill_y] = "|"
            next_sources.append((flow_x, fill_y))
            break
        grid[flow_x, fill_y] = "|"
    # detect suspicious situations
    # for ns_x, ns_y in next_sources.copy():
    #     if clay_left < ns_x < clay_right:
    #         next_sources.append((source_x, source_y))
    #         # transform every | into ~ on the horizontal of this source
    #         for suspicious_x in range(clay_left, clay_right):
    #             grid[suspicious_x, ns_y] = "~"
    return next_sources
    # check if we are in a disposition like #||||||||||||||#
    # if all(
    #     grid[check_x, fill_y] == "|" for check_x in range(clay_left + 1, clay_right)
    # ):
    #     for check_x in range(clay_left + 1, clay_right):
    #         grid[check_x, fill_y] = "~"
    #         # put previous source in todo list again
    #         draw_grid(grid)
    #         return [(source_x, source_y)]
    # else:
    #     return []


grid = parse_input(example_input)
sources = [(500, 0)]
seen_sources = set()
while len(sources):
    source = sources.pop(0)
    if source in seen_sources:
        continue
    seen_sources.add(source)
    print(f"source {source}")
    next_sources = evolve_grid(grid, *source)
    sources.extend(next_sources)
    debug_grid(grid)
debug_grid(grid)

grid = parse_input(raw_input)
sources = deque([(500, 0)])
count = 0
seen_sources = set()
while len(sources) > 0:
    source = sources.popleft()
    if source in seen_sources:
        continue
    seen_sources.add(source)
    next_sources = evolve_grid(grid, *source)
    sources.extend(next_sources)
    count += 1
    if count % 10 == 0:
        draw_grid(grid)
draw_grid(grid)