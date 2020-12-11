import copy

from PIL import Image, ImageDraw

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_layout = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def draw_grid(layout):
    imgFile = Image.new("RGB", (5 * len(layout[0]), 5 * len(layout)), (255, 255, 255))
    drawing = ImageDraw.Draw(imgFile)
    for y, row in enumerate(layout):
        for x, char in enumerate(row):
            if char == "L":
                color = "lightgreen"
            elif char == "#":
                color = "darkred"
            else:
                continue
            if x == 9 and y == 0:
                color = "purple"
            drawing.rectangle((5 * x, 5 * y, 5 * x + 3, 5 * y + 3), color)
    imgFile.show()


def calculate_next_grid(grid):
    new_grid = copy.deepcopy(grid)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == ".":  # floor: nobody sits here ever
                continue
            elif (
                char == "#"
            ):  # occupied seat: gets free if >= 4 adjacent seats occupied
                if adjacent_seats(x, y, grid).count("#") >= 4:
                    new_grid[y][x] = "L"
            elif char == "L":  # free seat: gets occupied if all adjacent seats are free
                if adjacent_seats(x, y, grid).count("#") == 0:
                    new_grid[y][x] = "#"
    return new_grid


def adjacent_seats(x, y, grid):
    offsets = {"x": [-1, 0, 1], "y": [-1, 0, 1]}
    if x == 0:
        offsets["x"].remove(-1)
    if y == 0:
        offsets["y"].remove(-1)
    if x >= len(grid[0]) - 1:
        offsets["x"].remove(1)
    if y >= len(grid) - 1:
        offsets["y"].remove(1)
    return [
        grid[adj_y][adj_x]
        for adj_x in (x + offset for offset in offsets["x"])
        for adj_y in (y + offset for offset in offsets["y"])
        if adj_x != x or adj_y != y
    ]


def count_occupied_seats(grid):
    return sum(row.count("#") for row in grid)


def search_stable_disposition(raw_layout):
    grid = [list(row) for row in raw_layout.splitlines()]
    occupied_seats = 0
    for i in range(100):
        grid = calculate_next_grid(grid)
        new_occupied_seats = count_occupied_seats(grid)
        if new_occupied_seats == occupied_seats:
            draw_grid(grid)
            return occupied_seats
        occupied_seats = new_occupied_seats


u.assert_equals(search_stable_disposition(example_layout), 37)
u.answer_part_1(search_stable_disposition(raw_input))

# draw_layout(raw_input.splitlines())

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
