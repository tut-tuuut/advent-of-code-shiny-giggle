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


def is_row_possible(symbols, digits):
    groups = []
    print(symbols)
    for char, group in groupby(list(symbols), lambda x: (x == ".")):
        if char != ".":
            groups.append("".join(group))
    groups = tuple(groups)
    group_lengths = tuple(len(g) for g in groups)
    print(groups, digits)
    # not enough chars
    if sum(digits) > sum(group_lengths):
        return False
    if any(digits) > max(group_lengths):
        return False
    return True


u.assert_equal(
    is_row_possible(".??..??...?##.", (1, 1, 3)), True, ".??..??...?##. 1,1,3"
)
u.assert_equal(is_row_possible("?.?.?.??", (1, 1, 3)), False, "no group long enough")
u.assert_equal(is_row_possible("??.?.?", (1, 2)), False, "Wrong order")
u.assert_equal(
    is_row_possible("????..##", (2, 2)), False, "Not enough place to separate groups"
)
u.assert_equal(
    is_row_possible("????", (2, 2)), False, "Not enough place to separate groups"
)


def analyze_row(row):
    symbols, digits = row.split(" ")
    groups = []
    for char, group in groupby(list(symbols), lambda x: (x == ".")):
        groups.append("".join(group))
    groups = tuple(groups)
    digits = tuple(int(d) for d in digits.split(","))
    print(groups, digits)


# analyze_row(".??..??...?##. 1,1,3")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
