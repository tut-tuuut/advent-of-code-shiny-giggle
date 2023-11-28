import math

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    grid = file.read().splitlines()

example_grid = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# first version: iterate over rows in grid, (A)
# ignore some of the rows if we are moving faster than 1 row at a time. (B)
# a bit of brainfuck to find the horizontal coordinate from the row number i.
# The most important part is the use of the property row[X] == row[X % len(pattern)] (C),
# which is true whenever a puzzle writer tells you that tere is a repeating pattern.
def how_many_trees_do_i_punch(grid, right_slope, down_slope):
    return sum(
        1
        for i, row in enumerate(grid)  # A
        if (row[(right_slope * i // down_slope) % len(row)] == "#")  # C
        and (i % down_slope == 0)  # B
    )


# second version: iterate over "time", the most understandable I think.
# vertical coordinate == row number in grid == time * down_slope (we move N rows down each time).
# horizontal coordinate == col number in row == time * right_slope (we move M columns each time).
# then like before, the "landscape" value at horiz coordinate X
# is the same as the "row" (pattern) at value X % len(row), hence the use of row[X % len(row)].
def how_many_trees_do_i_punch(grid, right_slope, down_slope):
    return sum(
        1
        for time in range(len(grid) // down_slope)
        if grid[time * down_slope][time * right_slope % len(grid[0])] == "#"
    )


# third version: iterate over row numbers, with an increment > 1 if down_slope > 1.
# back of the brainfuck of first version (// ftw), with even less clarity
# given the use of grid[row_num] instead of a variable row.
def how_many_trees_do_i_punch(grid, right_slope, down_slope):
    return sum(
        1
        for row_num in range(0, len(grid), down_slope)
        if grid[row_num][row_num * right_slope // down_slope % len(grid[0])] == "#"
    )


u.assert_equals(how_many_trees_do_i_punch(example_grid, 3, 1), 7)

u.answer_part_1(how_many_trees_do_i_punch(grid, 3, 1))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

expected_results_on_example_grid = (2, 7, 3, 4, 2)

for slope, result in zip(slopes, expected_results_on_example_grid):
    u.assert_equals(how_many_trees_do_i_punch(example_grid, *slope), result)

u.answer_part_2(math.prod(how_many_trees_do_i_punch(grid, *slope) for slope in slopes))
