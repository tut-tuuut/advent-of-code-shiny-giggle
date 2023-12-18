import utils as u
from collections import namedtuple, defaultdict, deque

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


def part_2(raw_input, reading_like="part_2", debug=True):
    # try "shoelace formula":
    # https://www.themathdoctors.org/polygon-coordinates-and-areas/
    for row in raw_input.strip().split("\n"):
        if reading_like == "part_1":
            direction, value, _ = row.split()
        else:
            direction = NB_TO_DIRECTION[int(row[-2])]
            value = int(row[-7:-2], 16)
            if debug:
                print(row, direction, value)


part_2(ex, debug=True)
