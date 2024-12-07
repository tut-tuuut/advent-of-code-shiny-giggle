import itertools
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def op_add(x, y):
    return x + y


def op_multiply(x, y):
    return x * y


def extract_lines(raw_str):
    for line in raw_str.splitlines():
        result_str, arguments_str = line.split(": ")
        arguments_int = tuple(int(xo) for xo in arguments_str.split())
        yield int(result_str), arguments_int


def part_1(raw_str, operators=(op_add, op_multiply)):
    calibration_result = 0
    for expected_result, operands in extract_lines(raw_str):
        for op_list in itertools.product(operators, repeat=len(operands) - 1):
            val = operands[0]
            for element, operator in zip(operands[1:], op_list):
                val = operator(val, element)
            if val == expected_result:
                calibration_result += expected_result
                break
    return calibration_result


u.assert_equal(part_1(example), 3749)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def op_concatenate(x, y):
    return int(f"{x}{y}")


def part_2(raw_str):
    operators = (op_add, op_multiply, op_concatenate)
    return part_1(raw_str, operators)


u.assert_equal(part_2(example), 11387)

u.answer_part_2(part_2(raw_input))
