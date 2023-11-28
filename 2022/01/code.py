from ast import parse
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_input(raw_input):
    return tuple(
        tuple(int(s) for s in number_str)
        for number_str in (
            group_str.split("\n") for group_str in raw_input.split("\n\n")
        )
    )


def part_1(raw_input):
    data = parse_input(raw_input)
    # Find the Elf carrying the most Calories.
    # How many total Calories is that Elf carrying?
    return max(sum(t) for t in data)


u.assert_equals(part_1(example_input), 24000)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(raw_input):
    data = parse_input(raw_input)
    # Find the top three Elves carrying the most Calories.
    # How many Calories are those Elves carrying in total?
    return sum(sorted((sum(t) for t in data), reverse=True)[:3])


u.assert_equals(part_2(example_input), 45000)
u.answer_part_2(part_2(raw_input))
