import itertools

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example_input = """199
200
208
210
200
207
240
269
260
263"""


def count_increased_measurements(raw_input):
    ints = [int(row) for row in raw_input.splitlines()]
    return sum(1 if ints[i + 1] > ints[i] else 0 for i in range(len(ints) - 1))


u.assert_equals(count_increased_measurements(example_input), 7)

u.answer_part_1(count_increased_measurements(raw_input))  # 1400

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# 0 1 2 3 4 5
# len 6
def count_increasing_windows(raw_input):
    ints = [int(row) for row in raw_input.splitlines()]
    window_sums = [sum(ints[i : i + 2]) for i in range(len(ints) - 1)]
    return sum(
        1 if window_sums[i + 1] > window_sums[i] else 0
        for i in range(len(window_sums) - 1)
    )


u.assert_equals(count_increasing_windows(example_input), 5)

u.answer_part_2(count_increasing_windows(raw_input))
# 1365 too low
# 1366 too low too
