import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

ex = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

N, S, E, W = "N", "S", "E", "W"

LEAVING = {
    "\\": {
        N: (W,),  # if I arrive on \ facing North, I go out facing West
        S: (E,),
        E: (S,),
        W: (N,),
    },
    "/": {
        N: (E,),
        S: (W,),
        E: (N,),
        W: (S,),
    },
    ".": {
        N: (N,),
        S: (S,),
        E: (E,),
        W: (W,),
    },
    "-": {
        N: (E, W),
        S: (E, W),
        E: (E,),
        W: (W,),
    },
    "|": {
        N: (N,),
        S: (S,),
        W: (N, S),
        E: (N, S),
    },
}


def get_next_position_from_direction(row, col, direction):
    if direction == N:
        row -= 1
    elif direction == S:
        row += 1
    elif direction == E:
        col += 1
    elif direction == W:
        col -= 1
    return row, col


def part_1(raw_input, debug=False):
    grid = tuple(raw_input.strip().split("\n"))
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    beam = [(0, -1, E)]
    energized = set()
    checked = set()
    while len(beam):
        row_i, col_j, direction = beam.pop()
        if ((row_i, col_j, direction)) in checked:
            continue
        checked.add((row_i, col_j, direction))
        energized.add((row_i, col_j))
        if debug:
            print(row_i, col_j, direction)
        next_i, next_j = get_next_position_from_direction(row_i, col_j, direction)
        if next_i < 0 or next_i >= HEIGHT or next_j < 0 or next_j >= WIDTH:
            continue
        next_position_content = grid[next_i][next_j]
        if debug:
            print(next_position_content)
        for new_direction in LEAVING[next_position_content][direction]:
            if debug:
                print("->", next_i, next_j, new_direction)
            beam.append((next_i, next_j, new_direction))
    if debug:
        for i in range(HEIGHT):
            print(i, end="")
            for j in range(WIDTH):
                if (i, j) in energized:
                    print(u.YELLOW, end="")
                print(grid[i][j], end="")
                print(u.CYAN, end="")
            print("")
    return len(energized) - 1


u.assert_equal(part_1(ex), 46)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
