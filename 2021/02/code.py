import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

raw_example = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def find_where_its_going(raw_input):
    x = 0
    depth = 0
    for row in raw_input.splitlines():
        value = int(row[-1:])
        dir = row[0]
        if dir == "f":
            x += value
        elif dir == "u":
            depth -= value
            if depth < 0:
                print("uh oh, flying submarine??")
        elif dir == "d":
            depth += value
    return x * depth


u.assert_equals(find_where_its_going(raw_example), 150)
u.answer_part_1(find_where_its_going(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def calculate_with_aim(raw_input):
    x = 0
    depth = 0
    aim = 0
    for row in raw_input.splitlines():
        value = int(row[-1:])
        dir = row[0]
        if dir == "f":
            x += value
            depth += value * aim
        elif dir == "u":
            aim -= value
        elif dir == "d":
            aim += value
    return x * depth


u.assert_equals(calculate_with_aim(raw_example), 900)
u.answer_part_2(calculate_with_aim(raw_input))
