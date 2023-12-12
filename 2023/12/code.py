import utils as u
from itertools import groupby

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

ex_ok = """#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1"""

ex_1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


SOLUTION = 3
POSSIBLE = 2
IMPOSSIBLE = False


def is_row_possible(symbols, digits):
    groups = []
    for is_dot, group in groupby(list(symbols), lambda x: (x == ".")):
        if not is_dot:
            groups.append("".join(group))
    groups = tuple(groups)
    group_lengths = tuple(len(g) for g in groups)
    if "?" not in symbols:
        if group_lengths == digits:
            return SOLUTION
        else:
            return IMPOSSIBLE
    if sum(digits) > sum(group_lengths):
        return IMPOSSIBLE
    if max(digits) > max(group_lengths):
        return IMPOSSIBLE
    return POSSIBLE


u.assert_equal(
    is_row_possible(".??..??...?##.", (1, 1, 3)), POSSIBLE, ".??..??...?##. 1,1,3"
)
u.assert_equal(
    is_row_possible("?.?.?.??", (1, 1, 3)), IMPOSSIBLE, "no group long enough"
)
u.assert_equal(is_row_possible("##.#.#", (2, 1, 1)), SOLUTION, "Is a solution")
u.assert_equal(is_row_possible("##.#.#", (2, 2, 1)), IMPOSSIBLE, "Is a wrong solution")


def analyze_row(row):
    symbols, digits = row.split(" ")
    digits = tuple(int(c) for c in digits.split(","))
    to_check = set()
    checked = set()
    solutions = set()

    to_check.add(symbols)
    while len(to_check):
        symbols = to_check.pop()
        checked.add(symbols)
        result = is_row_possible(symbols, digits)
        if result == SOLUTION:
            solutions.add(symbols)
        elif result == POSSIBLE:
            for char in (".", "#"):
                new_symbol = symbols.replace("?", char, 1)
                if not new_symbol in checked:
                    to_check.add(new_symbol)
    return len(solutions)


u.assert_equal(analyze_row(".??..??...?##. 1,1,3"), 4)


def part_1(raw_input):
    return sum(analyze_row(row) for row in raw_input.strip().split("\n"))


u.assert_equal(part_1(ex_1), 21)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
