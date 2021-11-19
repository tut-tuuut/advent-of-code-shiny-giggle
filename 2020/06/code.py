import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def count_distinct_yes_questions_in_group(group):
    # i would have loved to directly return
    # len(set(group).discard('\n'))
    # but discard() returns None...
    unique_chars = set(group)
    unique_chars.discard("\n")
    return len(unique_chars)


def count_distinct_yes_questions_in_group(group):
    # discard \n before counting unique characters
    return len(set(group.replace("\n", "")))


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


def count_unanimous_answers_in_group(group):
    individual_answers = group.splitlines()
    # we are looking for characters which are in *all* answers:
    # so they are in the first answer.
    first_answer = individual_answers[0]
    # count all characters of the first answer we can find in every answer.
    return sum(
        1
        for character in first_answer
        if all(character in answer for answer in individual_answers)
    )


def count_the_thingie_the_part_2_wants(airplane):
    return sum(
        count_unanimous_answers_in_group(group) for group in airplane.split("\n\n")
    )


u.assert_equals(count_unanimous_answers_in_group(example_group), 3)
u.assert_equals(count_the_thingie_the_part_2_wants(example_airplane), 6)

u.answer_part_2(count_the_thingie_the_part_2_wants(raw_input))
