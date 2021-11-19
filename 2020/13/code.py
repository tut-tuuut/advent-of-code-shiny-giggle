import re
import math

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


def extract_bus_lines_for_part_2(raw_postit):
    splitted_input = raw_postit.splitlines()
    if len(splitted_input) > 1:
        bus_lines = splitted_input[1]
    else:
        bus_lines = splitted_input[0]
    bus_lines = [
        (int(bus_line), position)
        for position, bus_line in enumerate(bus_lines.split(","))
        if bus_line != "x"
    ]
    bus_lines.sort()
    # bus_lines.reverse()
    return bus_lines


def win_the_shuttle_company_contest(bus_lines):
    slowest_bus_line, offset_slowest_bus_line = bus_lines.pop()
    # we will make these vary over bus lines
    timestamp = slowest_bus_line + offset_slowest_bus_line
    step = slowest_bus_line
    progress = 1
    print("█" * progress + "░" * (1 + len(bus_lines) - progress))
    for bus_line, expected_position in reversed(bus_lines):
        while timestamp % bus_line != expected_position % bus_line:
            # print(
            #     f"bus {bus_line} : expecting {expected_position}, got {timestamp % bus_line}"
            # )
            # ↑ this debug saved my computer & my afternoon from an endless loop
            # (it made me add the % bus_line after != expected_position)
            timestamp += step
        # now we've found a timestamp so that timestamp%bus_line == expected_position,
        # if we move timestamp using a multiple of bus_line, the modulo won't change!
        step = math.lcm(step, bus_line)
        progress += 1
        print("█" * progress + "░" * (1 + len(bus_lines) - progress) + f" {timestamp}")
    return abs(timestamp - step)  # why not just timestamp? I don't know
    #                                ↑ because I had pâté in my eyes


example_bus_lines = extract_bus_lines_for_part_2(example_postit)
u.assert_equals(win_the_shuttle_company_contest(example_bus_lines), 1068781),

other_example = extract_bus_lines_for_part_2("67,7,59,61")
other_examples = {
    "17,x,13,19": 3417,
    "67,7,59,61": 754018,
    "67,x,7,59,61": 779210,
    "67,7,x,59,61": 1261476,
    "1789,37,47,1889": 1202161486,
}
for lines, expected in other_examples.items():
    u.assert_equals(
        win_the_shuttle_company_contest(extract_bus_lines_for_part_2(lines)), expected
    )

u.answer_part_2(
    win_the_shuttle_company_contest(extract_bus_lines_for_part_2(raw_input))
)
# 905694340256752 returned by my function
# 455622713031375 is too low (timestamp)
