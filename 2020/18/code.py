import re
import math

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

CALCULUS_IN_PARENTHESIS = re.compile(r"\(([^()]+)\)")
ADDITION = re.compile(r"(\d+)\s+\+\s+(\d+)")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
# No precedence between operators except when there are parentheses


def calculate_with_christmas_precedence(calculus: str):
    # replace parenthesis with their calculus results
    while calculus.count("(") > 0:
        calculus = re.sub(
            CALCULUS_IN_PARENTHESIS,
            lambda m: f" {calculate_with_christmas_precedence(m.group(1))} ",
            calculus,
        )
    # calculate after parenthesis replacement
    elements = calculus.split()
    result = int(elements.pop(0))
    operator = ""
    for next_el in elements:
        if next_el in ("*", "+"):
            operator = next_el
        elif operator == "*":
            result *= int(next_el)
        elif operator == "+":
            result += int(next_el)
    return result


examples = {
    "1 + 2 * 3 + 4 * 5 + 6": 71,
    "2 * 3 + (4 * 5)": 26,
    "5 + (8 * 3 + 9 + 3 * 4 * 3)": 437,
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 12240,
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 13632,
}

for calculus, expected in examples.items():
    u.assert_equals(calculate_with_christmas_precedence(calculus), expected)

u.answer_part_1(
    sum(calculate_with_christmas_precedence(row) for row in raw_input.splitlines())
)
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
# """Advanced""" maths: + has precedence over *


def calculate_with_advanced_christmas_precedence(calculus: str):
    # replace parenthesis with their calculus results
    while calculus.count("(") > 0:
        calculus = re.sub(
            CALCULUS_IN_PARENTHESIS,
            lambda m: f" {calculate_with_advanced_christmas_precedence(m.group(1))} ",
            calculus,
        )
    # calculate addition results: look for substrings <number1> + <number2>
    # and replace them with <sum_of_the_two_numbers>
    while calculus.count("+") > 0:
        calculus = re.sub(
            ADDITION, lambda m: str(int(m.group(1)) + int(m.group(2))), calculus
        )
    # Sorry for the smarty oneliner below.
    # Explanation:
    # after above operations, calculus is now a string like 5 * 6 *... * 8
    # split it : it gives a list of strings '5','*','6'...
    # take one in two in this list: '5','6',... (I love Python)
    # map to int: 5,6...
    # and return the product of this map's elements
    return math.prod(map(int, calculus.split()[::2]))


def calculate_with_advanced_christmas_precedence(calculus: str):
    # replace parenthesis with their calculus results
    while calculus.count("(") > 0:
        calculus = re.sub(
            CALCULUS_IN_PARENTHESIS,
            lambda m: f" {calculate_with_advanced_christmas_precedence(m.group(1))} ",
            calculus,
        )
    return math.prod(
        sum(int(x) for x in sums.split("+")) for sums in calculus.split("*")
    )
    # with a map it works too:
    # return math.prod(sum(map(int, sums.split("+"))) for sums in calculus.split("*"))


examples = {
    "1 + 2 * 3 + 4 * 5 + 6": 231,
    "1 + (2 * 3) + (4 * (5 + 6))": 51,
    "2 * 3 + (4 * 5)": 46,
    "5 + (8 * 3 + 9 + 3 * 4 * 3)": 1445,
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 669060,
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 23340,
}

for calculus, expected in examples.items():
    u.assert_equals(calculate_with_advanced_christmas_precedence(calculus), expected)

u.answer_part_2(
    sum(
        calculate_with_advanced_christmas_precedence(row)
        for row in raw_input.splitlines()
    )
)
