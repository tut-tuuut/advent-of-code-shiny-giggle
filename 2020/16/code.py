import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

EXTRACT_CRITERIA = re.compile(r"\w+: (\d+)-(\d+) or (\d+)-(\d+)", re.MULTILINE)

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_valid_values_from_raw_input(raw_notes):
    valid_values = set()
    for low_from, low_to, top_from, top_to in (
        map(int, str_values) for str_values in EXTRACT_CRITERIA.findall(raw_notes)
    ):
        valid_values |= set(range(low_from, low_to + 1))
        valid_values |= set(range(top_from, top_to + 1))
    return valid_values


def compute_scanning_error_rate(raw_notes, valid_values):
    rows = raw_notes.splitlines()
    nearby_tickets_row = rows.index("nearby tickets:")
    invalid_values = []
    for raw_ticket in rows[nearby_tickets_row + 1 :]:
        invalid_values.extend(
            value
            for value in map(int, raw_ticket.split(","))
            if value not in valid_values
        )
    return sum(invalid_values)


valid_values = extract_valid_values_from_raw_input(example_input)
u.assert_equals(compute_scanning_error_rate(example_input, valid_values), 71)

my_valid_values = extract_valid_values_from_raw_input(raw_input)
u.answer_part_1(compute_scanning_error_rate(raw_input, my_valid_values))
# 16908 too low: i will try use a list instead of a set

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
