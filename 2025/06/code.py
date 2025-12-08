import utils as u
import numpy as np
from math import prod

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def part_1(given_input):
    given_input_as_tuple = tuple(given_input.splitlines())
    arr = np.array(
        tuple(
            tuple(int(cell) for cell in row.split())
            for row in given_input_as_tuple[:-1]
        )
    )
    numbers = arr.transpose()
    operators = given_input_as_tuple[-1].split()
    return sum(
        (sum(operands) if (operator == "+") else prod(operands))
        for operator, operands in zip(operators, numbers)
    )


u.assert_equal(part_1(example), 4277556)

u.answer_part_1(part_1(raw_input))


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def yield_numbers_from_sheet(sheet):
    stocked_numbers = []
    for row in sheet:
        if row == "":
            yield stocked_numbers
            stocked_numbers = []
        else:
            stocked_numbers.append(int(row))
    yield stocked_numbers


def part_2(given_input):
    given_input_as_tuple = tuple(given_input.splitlines())
    arr = np.array(
        tuple(
            tuple(int(cell) if cell.isdigit() else "" for cell in row)
            for row in given_input_as_tuple[:-1]
        )
    )
    numbers_as_str = list("".join(row) for row in arr.transpose())
    operators = given_input_as_tuple[-1].split()
    return sum(
        (sum(operands) if (operator == "+") else prod(operands))
        for operator, operands in zip(
            operators, yield_numbers_from_sheet(numbers_as_str)
        )
    )


u.assert_equal(part_2(example), 3263827)

u.answer_part_2(part_2(raw_input))
