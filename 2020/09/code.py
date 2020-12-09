import more_itertools

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()
example_raw_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_first_invalid_number(raw_input, preamble_length):
    """Find the first number in raw_input which is not the sum
    of two of the {preamble_length} previous numbers"""

    # use a sliding window of length 1 + preamble_length:
    # last element of the window will be the currently checked number,
    # against the {preamble_length} others
    for window in more_itertools.windowed(
        map(int, raw_input.splitlines()), 1 + preamble_length
    ):
        if not check_number_validity(window[-1], window[:-1]):
            return window[-1]


def check_number_validity(number, previous_numbers):
    """Return true if two numbers of previous_numbers sum up exactly to number"""
    for candidate in previous_numbers:
        if number - candidate in previous_numbers:
            return True
    return False


u.assert_equals(extract_first_invalid_number(example_raw_input, 5), 127)

u.answer_part_1(extract_first_invalid_number(raw_input, 25))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
