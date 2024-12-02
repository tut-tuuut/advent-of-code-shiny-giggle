import utils as u
from itertools import pairwise

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def is_safe(row_str):
    numbers = tuple(int(car) for car in row_str.split())
    diffs = tuple(x - y for x, y in pairwise(numbers))
    if not all(0 < abs(diff) < 4 for diff in diffs):
        return False
    return all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)


def part_1(input_str):
    return sum(1 for row_str in input_str.splitlines() if is_safe(row_str))


u.assert_equal(part_1(example), 2)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
