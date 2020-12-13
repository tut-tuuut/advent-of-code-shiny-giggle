import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_postit = """939
7,13,x,x,59,x,31,19"""


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_schedule_and_bus_lines(raw_postit):
    schedule, bus_lines = raw_postit.splitlines()
    schedule = int(schedule)
    bus_lines = [int(x) for x in re.findall(r"\d+", bus_lines)]
    return [schedule, bus_lines]


def answer_part_1(schedule, bus_lines):
    number_of_minutes, bus_id = min((x - schedule % x, x) for x in bus_lines)
    return number_of_minutes * bus_id


u.assert_equals(answer_part_1(*extract_schedule_and_bus_lines(example_postit)), 295)

actual_data = extract_schedule_and_bus_lines(raw_input)
u.answer_part_1(answer_part_1(*actual_data))


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
