import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def count_distinct_yes_questions_in_group(group):
    unique_chars = set(group)
    unique_chars.discard("\n")
    return len(unique_chars)


def count_the_thingie_the_part_1_wants(airplane):
    return sum(
        count_distinct_yes_questions_in_group(group) for group in airplane.split("\n\n")
    )


example_group = """abcx
abcy
abcz"""

u.assert_equals(
    count_distinct_yes_questions_in_group(example_group),
    6,
)

example_airplane = """abc

a
b
c

ab
ac

a
a
a
a

b"""

u.assert_equals(count_the_thingie_the_part_1_wants(example_airplane), 11)

u.answer_part_1(count_the_thingie_the_part_1_wants(raw_input))

print(len(raw_input.split("\n\n")))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
