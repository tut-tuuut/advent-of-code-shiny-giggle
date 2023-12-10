import utils as u
from itertools import pairwise

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def part_1(raw_input):
    result_sum = 0
    for row in raw_input.strip().split("\n"):
        digits = list(int(x) for x in row.split())
        digit_list = list()
        digit_list.append(digits)
        while any(d != 0 for d in digits):
            diffs = list(b - a for a, b in pairwise(digits))
            digits = diffs
            digit_list.insert(0, digits)
        print(f"{len(digit_list)} derivations…")
        for i, values in enumerate(digit_list[:-1]):
            digit_list[i + 1].append(values[-1] + digit_list[i + 1][-1])
        result_sum += digit_list[-1][-1]
    return result_sum


u.assert_equal(part_1(example_input), 114)

u.answer_part_1(part_1(raw_input))

# 1702219394 too high, I checked d > 0 instead of d != 0

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
