import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_row_value(row, with_letters=False):
    indexes = dict()
    for digit in range(1, 10):
        s = str(digit)
        if s in row:
            indexes[row.find(s)] = digit
            indexes[row.rfind(s)] = digit
    if with_letters:
        for s, digit in (
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9),
        ):
            if s in row:
                indexes[row.find(s)] = digit
                indexes[row.rfind(s)] = digit
    keys = indexes.keys()
    return_value = 10 * indexes[min(keys)] + indexes[max(keys)]
    return return_value


u.assert_equal(extract_row_value("smm2dlsmfkj42"), 22)
u.assert_equal(extract_row_value("dsqlj8fdlskj"), 88)


def calibration_value(input, with_letters=False):
    return sum(extract_row_value(row, with_letters) for row in input.split())


u.assert_equal(calibration_value(example_input_1), 142)

u.answer_part_1(calibration_value(raw_input))
# 53958 too low

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example_input_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def extract_row_value_with_letters(row):
    return extract_row_value(row, True)


u.assert_equal(extract_row_value_with_letters("two1nine"), 29)
u.assert_equal(extract_row_value_with_letters("twoone"), 21)
u.assert_equal(extract_row_value_with_letters("fiveight"), 58)

u.answer_part_2(calibration_value(raw_input, True))
