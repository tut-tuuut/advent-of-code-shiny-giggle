import copy
import random

from PIL import Image, ImageDraw
import networkx as nx

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


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

DIRECTIONS = (
    (-1, -1),  # nw
    (0, -1),  # n
    (1, -1),  # ne
    (1, 0),  # e
    (1, 1),  # se
    (0, 1),  # s
    (-1, 1),  # sw
    (-1, 0),  # w
)
# you can compute visibilities only once: they don't change
# when seats get occupied or freed.
# store them in a graph to be able to use node.neighbors(), it will be useful
def compute_visibilities(grid):
    """Compute line views for every seat and return them in a networkx.graph"""
    visibilities = nx.Graph()
    grid_size = max(len(grid), len(grid[0]))
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == ".":
                continue
            for dirx, diry in DIRECTIONS:
                in_grid = True
                no_seat_encountered = True
                distance = 0
                while in_grid and no_seat_encountered:
                    distance += 1
                    target_y = y + distance * diry
                    target_x = x + distance * dirx
                    if (
                        target_y < 0
                        or target_y >= len(grid)
                        or target_x < 0
                        or target_x >= len(grid[0])
                    ):
                        in_grid = False
                        continue
                    if grid[target_y][target_x] == "L":
                        no_seat_encountered = False
                        visibilities.add_edge((x, y), (target_x, target_y))
    return visibilities


def draw_grid_with_visibilities(grid, visibility_graph):
    scale = 15
    seat_size = 5
    imgFile = Image.new(
        "RGB", (scale * len(grid[0]), scale * len(grid)), (255, 255, 255)
    )
    drawing = ImageDraw.Draw(imgFile)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "L":
                color = "black"
            elif char == "#":
                color = "darkred"
            else:
                continue
            drawing.rectangle(
                (scale * x, scale * y, scale * x + seat_size, scale * y + seat_size),
                color,
            )
    for u, v in visibility_graph.edges():
        # if u[0] % 3 > 0 and v[0] % 3 > 0:
        #    continue
        # if u[1] % 3 > 0 and v[1] % 3 > 0:
        #    continue
        drawing.line(
            (
                seat_size // 2 + u[0] * scale,
                seat_size // 2 + u[1] * scale,
                seat_size // 2 + v[0] * scale,
                seat_size // 2 + v[1] * scale,
            ),
            random.choice(
                [
                    "chartreuse",
                    "skyblue",
                    "blue",
                    "red",
                    "pink",
                    "lime",
                    "purple",
                    "orange",
                ]
            ),
        )
    imgFile.show()


def visible_seats(x, y, grid, visibilities):
    return [grid[y][x] for x, y in visibilities.neighbors((x, y))]


def calculate_next_grid_for_part_two(grid, visibilities):
    new_grid = copy.deepcopy(grid)
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == ".":  # floor: nobody sits here ever
                continue
            elif char == "#":
                # occupied seat: gets free if >= 5 visible seats occupied
                if visible_seats(x, y, grid, visibilities).count("#") >= 5:
                    new_grid[y][x] = "L"
            elif char == "L":
                # free seat: gets occupied if all visible seats are free
                if visible_seats(x, y, grid, visibilities).count("#") == 0:
                    new_grid[y][x] = "#"
    return new_grid


def search_stable_disposition_for_part_two(raw_layout):
    grid = [list(row) for row in raw_layout.splitlines()]
    visibilities = compute_visibilities(grid)
    occupied_seats = 0
    for i in range(100):
        grid = calculate_next_grid_for_part_two(grid, visibilities)
        new_occupied_seats = count_occupied_seats(grid)
        if new_occupied_seats == occupied_seats:
            draw_grid(grid)
            return occupied_seats
        occupied_seats = new_occupied_seats


u.assert_equals(search_stable_disposition_for_part_two(example_layout), 26)

u.answer_part_2(search_stable_disposition_for_part_two(raw_input))
