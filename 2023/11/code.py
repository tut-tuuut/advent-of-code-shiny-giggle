import utils as u
from itertools import combinations

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

ex = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_input(raw_input):
    # print(raw_input)
    grid = tuple(raw_input.strip().split("\n"))
    empty_cols = set(
        j
        for j in range(len(grid[0]))
        if all(grid[i][j] == "." for i in range(len(grid)))
    )
    empty_rows = set(
        i
        for i in range(len(grid))
        if all(grid[i][j] == "." for j in range(len(grid[0])))
    )
    galaxies = {
        (i, j)
        for j in range(len(grid[0]))
        for i in range(len(grid))
        if grid[i][j] == "#"
    }
    # print(empty_cols, empty_rows, galaxies)
    return empty_cols, empty_rows, galaxies


parse_input(ex)


def part_1(raw_input, expansion_factor=1):
    empty_cols, empty_rows, galaxies = parse_input(raw_input)
    total_dist = 0
    for ga, gb in combinations(galaxies, 2):
        dist = abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])
        dist += sum(
            expansion_factor
            for e in empty_cols
            if ga[1] < e < gb[1] or gb[1] < e < ga[1]
        )
        dist += sum(
            expansion_factor
            for e in empty_rows
            if ga[0] < e < gb[0] or gb[0] < e < ga[0]
        )
        total_dist += dist
    return total_dist


u.assert_equal(part_1(ex), 374)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.assert_equal(part_1(ex, expansion_factor=9), 1030)
u.assert_equal(part_1(ex, expansion_factor=99), 8410)

u.answer_part_2(part_1(raw_input, expansion_factor=(1000000 - 1)))
