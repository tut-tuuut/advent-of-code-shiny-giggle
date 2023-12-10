import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

example_2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def format_for_human(input_str):
    return (
        input_str.replace(".", " ")
        .replace("-", "─")
        .replace("|", "│")
        .replace("7", "┐")
        .replace("F", "┌")
        .replace("L", "└")
        .replace("J", "┘")
    )


def parse_input(raw_input):
    rows = tuple(raw_input.strip().split())
    for i, row in enumerate(rows):
        if "S" in row:
            s_coords = (i, row.index("S"))
            return rows, s_coords


def part_1(raw_input):
    N, S, E, W = "N", "S", "E", "W"
    connections = {
        "S": {N, S, E, W},
        "|": {N, S},
        "F": {S, E},
        "L": {N, E},
        "J": {N, W},
        "7": {W, S},
        "-": {E, W},
        ".": set(),
    }

    def find_connected_neighbours(coords):
        i, j = coords
        current_point = rows[i][j]
        to_check = connections[current_point]
        if N in to_check and i > 0:
            if S in connections[rows[i - 1][j]]:
                yield ((i - 1, j))
        if W in to_check and j > 0:
            if E in connections[rows[i][j - 1]]:
                yield ((i, j - 1))
        if E in to_check and j < len(rows[i]) - 1:
            if W in connections[rows[i][j + 1]]:
                yield ((i, j + 1))
        if S in to_check and i < len(rows) - 1:
            if N in connections[rows[i + 1][j]]:
                yield ((i + 1, j))

    rows, s_coords = parse_input(raw_input)
    the_loop = set()
    the_loop.add(s_coords)
    to_test = set()
    for x in find_connected_neighbours(s_coords):
        to_test.add(x)
    while len(to_test) > 0:
        x = to_test.pop()
        the_loop.add(x)
        for z in find_connected_neighbours(x):
            if not z in the_loop:
                to_test.add(z)
    return int(len(the_loop) / 2)


u.assert_equal(part_1(example_1), 4)
u.assert_equal(part_1(example_2), 8)
u.answer_part_1(part_1(raw_input))
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
