import utils as u
from collections import namedtuple, defaultdict, deque
from itertools import pairwise

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

ex = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
R, L, U, D = "R", "L", "U", "D"
Point = namedtuple("Point", ("i", "j"))
DIRECTIONS = {
    R: Point(0, +1),
    L: Point(0, -1),
    D: Point(+1, 0),
    U: Point(-1, 0),
}


def add_points(a, b, length=1):
    return Point(a.i + b.i * length, a.j + b.j * length)


def vec(a, b):  # vector from point a to b
    return Point(b.i - a.i, b.j - a.j)


def det(a, b):  # determinant between two vectors (no interest for points)
    return a.i * b.j - b.i * a.j


def draw_grid(grid: defaultdict):
    min_i = min(p.i for p in grid.keys())
    max_i = max(p.i for p in grid.keys())
    min_j = min(p.j for p in grid.keys())
    max_j = max(p.j for p in grid.keys())

    return "\n".join(
        (
            "".join(grid[Point(i, j)] for j in range(min_j, max_j + 1))
            for i in range(min_i, max_i + 1)
        )
    )


def part_1(raw_input, debug=False):
    current_point = Point(0, 0)
    grid = defaultdict(lambda: ".")
    grid[current_point] = "#"
    for row in raw_input.strip().split("\n"):
        direction, value, color = row.split()
        for _ in range(int(value)):
            current_point = add_points(current_point, DIRECTIONS[direction])
            grid[current_point] = "#"
    if debug:
        print(draw_grid(grid))
    to_check = deque()
    checked = set()
    min_i = min(p.i for p in grid.keys())
    max_i = max(p.i for p in grid.keys())
    min_j = min(p.j for p in grid.keys())
    max_j = max(p.j for p in grid.keys())
    for j in range(min_j, max_j + 1):
        to_check.append((min_i, j))
        to_check.append((max_i, j))
    for i in range(min_i, max_i + 1):
        to_check.append((i, min_j))
        to_check.append((i, max_j))

    while len(to_check):
        i, j = to_check.pop()
        checked.add((i, j))
        if i < min_i or i > max_i or j < min_i or j > max_j:
            continue
        if grid[Point(i, j)] == ".":
            grid[Point(i, j)] = " "
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if (r, c) not in checked:
                        to_check.append((r, c))
    if debug:
        print(draw_grid(grid))
    else:
        draw_grid(grid)
    return sum(1 for val in grid.values() if val != " ")


u.assert_equal(part_1(ex), 62)
# u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

NB_TO_DIRECTION = (R, D, L, U)


def part_2(raw_input, reading_like="part_2", debug=False):
    # try "shoelace formula":
    # https://www.themathdoctors.org/polygon-coordinates-and-areas/
    # ---- build list of points
    points = []
    current_point = Point(0, 0)
    points.append(current_point)
    for row in raw_input.strip().split("\n"):
        if reading_like == "part_1":
            direction, value, _ = row.split()
            value = int(value)
        else:
            direction = NB_TO_DIRECTION[int(row[-2])]
            value = int(row[-7:-2], 16)
        if debug:
            print(row, direction, value)
        new_point = add_points(current_point, DIRECTIONS[direction], value)
        points.append(new_point)
        current_point = new_point
    u.assert_equal(points[0], points[-1], "path should be closed")
    u.assert_equal(
        len(points) - 1,
        len(set(points)),
        "all points should be distinct except last one",
    )
    if debug:
        print(points)
    # --- calculate base area using shoelace formula
    double_area = abs(sum(a.i * b.j - a.j * b.i for a, b in pairwise(points)))
    # --- add "outer" area (1/2*perimeter)
    double_area += sum(abs(a.i - b.i + a.j - b.j) for a, b in pairwise(points))
    # --- adjust corners (+0,25/obtus corner -0,25/closed corner)
    determinants = []
    for i in range(1, len(points) - 1):
        a = points[i - 1]
        b = points[i]
        c = points[(i + 1) % len(points)]
        v1 = vec(a, b)
        v2 = vec(b, c)
        determinants.append(det(v1, v2))
    corner_area = 1
    corner_area += sum(1 for d in determinants if d < 0)
    corner_area -= sum(1 for d in determinants if d > 0)
    quadruple_area = 2 * double_area + corner_area
    print("quadruple area", quadruple_area, quadruple_area / 4)
    if debug:
        grid = defaultdict(lambda: ".")
        for p in points:
            grid[p] = "#"
        print(draw_grid(grid))
    return int(quadruple_area / 4)


part_1(ex, debug=True)
u.assert_equal(part_2(ex, debug=True, reading_like="part_1"), 62)
u.assert_equal(part_2(raw_input, reading_like="part_1"), 70026)
# part_2(raw_input, debug=False, reading_like="part_1")
u.assert_equal(part_2(ex), 952408144115)
u.answer_part_2(part_2(raw_input))
