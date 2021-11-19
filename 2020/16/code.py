import re
from math import prod

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
EXTRACT_FIELDS = re.compile(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", re.MULTILINE)

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


def extract_valid_tickets(raw_notes, valid_values):
    rows = raw_notes.splitlines()
    nearby_tickets_row = rows.index("nearby tickets:")
    for raw_ticket in rows[nearby_tickets_row + 1 :]:
        int_ticket = tuple(map(int, raw_ticket.split(",")))
        if all(value in valid_values for value in int_ticket):
            yield (int_ticket)


def extract_my_ticket_from_raw_input(raw_input):
    rows = raw_input.splitlines()
    my_ticket_row = rows.index("your ticket:")
    return tuple(map(int, rows[my_ticket_row + 1].split(",")))


def extract_valid_values_per_fields_from_raw_input(raw_notes):
    valid_values = {}
    for field_name, low_from, low_to, top_from, top_to in EXTRACT_FIELDS.findall(
        raw_notes
    ):
        valid_values[field_name] = set(range(int(low_from), int(low_to) + 1)) | set(
            range(int(top_from), int(top_to) + 1)
        )
    return valid_values


def relate_fields_to_values_in_ticket(raw_input):
    valid_values = extract_valid_values_from_raw_input(raw_input)
    my_ticket = extract_my_ticket_from_raw_input(raw_input)
    fields_possible_values = extract_valid_values_per_fields_from_raw_input(raw_input)
    fields_possible_positions = {
        field: set(range(len(my_ticket))) for field in fields_possible_values
    }
    fields_positions = {}
    # reduce possible positions for each field using my (valid!) ticket
    for position, value in enumerate(my_ticket):
        for field, possible_values in fields_possible_values.items():
            if value not in possible_values:
                fields_possible_positions[field].remove(position)
    # reduce possible positions for each field using nearby tickets
    for ticket in extract_valid_tickets(raw_input, valid_values):
        for position, value in enumerate(ticket):
            for field, possible_values in fields_possible_values.items():
                if value not in possible_values:
                    fields_possible_positions[field].remove(position)
    # now we reduce the possible positions: if a field has only ONE possible position,
    # this position is not possible for other fields.
    while len(fields_possible_positions):
        for field in fields_possible_positions:
            if len(fields_possible_positions[field]) == 1:
                position_for_field = fields_possible_positions[field].pop()
                fields_positions[field] = position_for_field
                for other_field in fields_possible_positions:
                    fields_possible_positions[other_field].discard(position_for_field)
        fields_possible_positions = {
            k: v for k, v in fields_possible_positions.items() if len(v) > 0
        }
    # And now we have the positions, do not forget to map them to the values...
    fields_values = {
        key: my_ticket[position] for key, position in fields_positions.items()
    }
    return fields_values


example_input = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

example_values = relate_fields_to_values_in_ticket(example_input)
u.assert_equals(example_values, {"class": 12, "row": 11, "seat": 13})


my_values = relate_fields_to_values_in_ticket(raw_input)
u.answer_part_2(
    prod(val for key, val in my_values.items() if key.startswith("departure"))
)
# 45696 too low (I made a product of the positions instead of the values, duh)
# 1307550234719 is the right answer, indeed the previous one was too low
