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


def extract_loop(raw_input):
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
    return the_loop


def part_1(raw_input):
    the_loop = extract_loop(raw_input)
    return int(len(the_loop) / 2)


u.assert_equal(part_1(example_1), 4)
u.assert_equal(part_1(example_2), 8)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2_excel(raw_input):
    """attempt to format the thing in csv format to hand check connections on excel"""
    rows, s_coords = parse_input(raw_input)
    the_loop = extract_loop(raw_input)
    human_input = format_for_human(raw_input)
    list_of_points = list(list(row) for row in human_input.split("\n"))
    for i, row in enumerate(rows):
        for j, _ in enumerate(row):
            if (i, j) in the_loop:
                list_of_points[i][j] = "x"
    human_output = "\n".join(",".join(row) for row in list_of_points)
    print(human_output)


# part_2_excel(raw_input)

"""
try something like a transformation of the data ?
one square is changed into 9 squares

        ......
┌┐   -> .████.
        .█..█.

"""


def part_2_bigger_grid(raw_input):
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
    # -----
    the_loop = extract_loop(raw_input)
    human_input = format_for_human(raw_input)
    print(human_input)
    list_of_points = tuple(raw_input.strip().split())
    tripled_map = []
    for i, row in enumerate(list_of_points):
        tripled_row = [[] for _ in range(3)]
        for j, p in enumerate(row):
            points = [[".", ".", "."] for _ in range(3)]
            if (i, j) in the_loop:
                u.pink(f"{i}-{j} in the loop : {p}")
                points[1][1] = "█"
                if N in connections[p]:
                    points[0][1] = "█"
                if S in connections[p]:
                    points[2][1] = "█"
                if E in connections[p]:
                    points[1][2] = "█"
                if W in connections[p]:
                    points[1][0] = "█"
                print("\n".join("".join(r) for r in points))
            for a in range(3):
                tripled_row[a].extend(points[a])
        tripled_map.extend(tripled_row)
    print("\n".join("".join(tripled_row) for tripled_row in tripled_map))


part_2_bigger_grid(
    """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
)

part_2_bigger_grid(
    """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

"""
)

part_2_bigger_grid(raw_input)
