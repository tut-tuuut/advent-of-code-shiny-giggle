import utils as u
from collections import namedtuple, defaultdict

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


def add_points(a, b):
    return Point(a.i + b.i, a.j + b.j)


def draw_grid(grid: defaultdict):
    min_i = min(p.i for p in grid.keys())
    max_i = max(p.i for p in grid.keys())
    min_j = min(p.j for p in grid.keys())
    max_j = max(p.j for p in grid.keys())

    return "\n".join(
        (
            "".join(grid[Point(i, j)] for j in range(min_j - 1, max_j + 1))
            for i in range(min_i - 1, max_i + 1)
        )
    )


def part_1(raw_input):
    current_point = Point(0, 0)
    grid = defaultdict(lambda: ".")
    grid[current_point] = "#"
    for row in raw_input.strip().split("\n"):
        direction, value, color = row.split()
        for _ in range(int(value)):
            current_point = add_points(current_point, DIRECTIONS[direction])
            grid[current_point] = "#"
    print(draw_grid(grid))


part_1(ex)

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
