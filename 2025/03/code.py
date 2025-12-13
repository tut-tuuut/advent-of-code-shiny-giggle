import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example = """987654321111111
811111111111119
234234234234278
818181911112111"""


def joltage(given_str):
    for first_digit in reversed(range(1, 10)):
        idx = given_str[:-1].find(str(first_digit))
        if idx >= 0:
            for second_digit in reversed(range(1, 10)):
                second_idx = given_str[idx + 1 :].find(str(second_digit))
                if second_idx >= 0:
                    return 10 * first_digit + second_digit


u.assert_equal(joltage("987654321111111"), 98)
u.assert_equal(joltage("811111111111119"), 89)
u.assert_equal(joltage("234234234234278"), 78)
u.assert_equal(joltage("818181911112111"), 92)


def part_1(given_input):
    return sum(joltage(row) for row in given_input.splitlines())


u.assert_equal(part_1(example), 357)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def joltage_recur(given_str, remaining):
    if remaining <= 0:
        return []
    for first_digit in reversed(range(1, 10)):
        if remaining > 1:
            idx = given_str[: -(remaining - 1)].find(str(first_digit))
        else:
            idx = given_str.find(str(first_digit))
        if idx >= 0:
            other_digits = joltage_recur(given_str[idx + 1 :], remaining - 1)
            return [first_digit, *other_digits]


u.assert_equal(joltage_recur("987654321111111", 2), [9, 8])
u.assert_equal(joltage_recur("811111111111119", 2), [8, 9])
u.assert_equal(joltage_recur("234234234234278", 2), [7, 8])
u.assert_equal(joltage_recur("818181911112111", 2), [9, 2])


def part_2(given_input):
    return sum(
        int("".join(str(digit) for digit in joltage_recur(row, 12)))
        for row in given_input.splitlines()
    )


u.assert_equal(part_2(example), 3121910778619)

u.answer_part_2(part_2(raw_input))
