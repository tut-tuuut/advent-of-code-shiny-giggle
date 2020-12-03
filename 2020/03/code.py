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


def how_many_trees_do_i_punch(grid, right_slope, down_slope):
    return sum(
        1
        for i, row in enumerate(grid)
        if (row[(right_slope * i // down_slope) % len(row)] == "#")
        and (i % down_slope == 0)
    )


u.assert_equals(how_many_trees_do_i_punch(example_grid, 3, 1), 7)

u.answer_part_1(how_many_trees_do_i_punch(grid, 3, 1))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

expected_results_on_example_grid = (2, 7, 3, 4, 2)

for slope, result in zip(slopes, expected_results_on_example_grid):
    u.assert_equals(how_many_trees_do_i_punch(example_grid, *slope), result)

u.answer_part_2(math.prod(how_many_trees_do_i_punch(grid, *slope) for slope in slopes))
