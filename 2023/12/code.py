import utils as u
from itertools import groupby
import re
from functools import cache

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


# return a simplified version of the row,
# using my own brain algorithm of when i play picross.
def picross_row(symbols, digits, debug=False):
    if debug:
        print("calling picross row with ", symbols, digits)
    if len(digits) == 0:
        return "#", (1,)  # unique solution
    # remove empty spaces at start and end, we don't care
    symbols = symbols.strip(".")
    total_space_needed = sum(digits) + len(digits) - 1
    freedom_degrees = len(symbols) - total_space_needed
    if freedom_degrees == 0:  # huzzah EASYPEASY
        return ".".join("#" * d for d in digits), digits
    if freedom_degrees >= max(digits):  # no easy solution :'(
        return symbols, digits
    if symbols[0] == "#":
        # we know the beginning of the row,
        # we remove it with its digit and we try to simplify more!
        return picross_row(symbols[1 + digits[0] :], digits[1:])
    if symbols[-1] == "#":
        # we know the end of the row:
        # we remove it with its digit, and we simplify more
        return picross_row(symbols[: -1 - digits[-1]], digits[:-1])
    return symbols, digits
    # now, "count blocks" and see if we find results
    cursor = 0
    computed_blocks = []
    print("freedom", freedom_degrees)
    for d in digits:
        print(f"block of {d} ----")
        if d <= freedom_degrees:
            print("append", symbols[cursor : cursor + d + 1])
            computed_blocks.append(symbols[cursor : cursor + d + 1])
        else:
            print("append unknown", symbols[cursor : cursor + freedom_degrees])
            computed_blocks.append(symbols[cursor : cursor + freedom_degrees])
            print("fill", "#" * (d - freedom_degrees))
            computed_blocks.append("#" * (d - freedom_degrees))
            computed_blocks.append(symbols[cursor + d : cursor + d + 1])
        cursor += d + 1  # one block + one hole
    print("after ", "".join(computed_blocks))
    print("before", symbols)
    return symbols, digits


# u.assert_equal(picross_row(".??????.", (3, 2)), ("###.##", (3, 2)))
print(picross_row("....?#?#?#?#?#?#?#?..", (1, 3, 1, 6)))
# print(picross_row("#???..?", (3, 1)))
# print(picross_row("????#", (1, 2)))
picross_row("????????????", (2, 6))


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

    groups_of_hashes = tuple(group for group in groups if "?" not in group)
    if any(len(hashgroup) not in digits for hashgroup in groups_of_hashes):
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


def analyze_row(row, debug=False):
    bef = u.nanotime()
    symbols, digits = row.split(" ")
    digits = tuple(int(c) for c in digits.split(","))
    symbols, digits = picross_row(symbols, digits)
    to_check = set()
    checked = set()
    solutions = set()

    to_check.add(symbols)
    while len(to_check):
        symbols = to_check.pop()
        checked.add(symbols)
        if symbols.count("#") == sum(digits):
            symbols = symbols.replace("?", ".")
        result = is_row_possible(symbols, digits)
        if result == SOLUTION:
            solutions.add(symbols)
        elif result == POSSIBLE:
            for char in (".", "#"):
                new_symbol = symbols.replace("?", char, 1)
                if not new_symbol in checked:
                    to_check.add(new_symbol)
    aft = u.nanotime()
    row_time = (aft - bef) / 10**6
    if debug:
        print(
            f"checked {len(checked)} possibilities for {len(solutions)} solutions in {row_time} ms"
        )
    return len(solutions)


u.assert_equal(analyze_row(".??..??...?##. 1,1,3"), 4)


def part_1(raw_input):
    result = 0
    before = u.nanotime()
    for row in raw_input.strip().split("\n"):
        result += analyze_row(row)
    after = u.nanotime()
    total_time = after - before
    print(f"total time {total_time/10**9} s")
    return result


u.assert_equal(part_1(ex_1), 21)

# u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def expand_row(row):
    symbols, digits = row.split(" ")
    return f"{'?'.join(symbols for _ in range(5))} {','.join(digits for _ in range(5))}"


def part_2(raw_input):
    u.nanotime()
    i = 0
    result = 0
    for row in raw_input.split("\n"):
        print(f"{i}")
        print(u.nanotime())
        i += 1
        expanded_row = expand_row(row)
        result += analyze_row(expanded_row)
    return result


# part_2(".??..??...?##. 1,1,3")
# u.assert_equal(part_2(ex_1), 525152)

REGEX = re.compile(r"[\?#]+")


@cache
def analyze_row_clever(symbols, digits, debug=False):
    if debug:
        print("analyzing", symbols, digits)

    if len(digits) == 0:
        if symbols.count("#") == 0:
            return 1
        else:
            return 0

    if symbols.count("#") + symbols.count("?") < sum(digits):
        return 0

    symbols = symbols.strip(".")

    pattern = re.compile("([?#]{%d})([?.]|$)" % digits[0])
    if debug:
        print(pattern)
    first_match = pattern.search(symbols)
    if first_match is None:
        return 0
    if debug:
        print("match :", first_match[0])
        print("start and end:", first_match.start(), first_match.end())
    if symbols[: first_match.start()].count("#") > 0:
        return 0
    solutions = analyze_row_clever(symbols[first_match.end() :], digits[1:])
    if symbols[first_match.start()] == "?":
        other_solutions = analyze_row_clever(
            symbols[first_match.start() + 1 :], digits, debug
        )
    else:
        other_solutions = 0
    return solutions + other_solutions


print("-----part2-----")

u.assert_equal(analyze_row_clever("?#...###", (1, 3), True), 1)

u.assert_equal(analyze_row_clever("???.###", (1, 1, 3)), 1)
u.assert_equal(analyze_row_clever(".??..??...?##.", (1, 1, 3)), 4)
u.assert_equal(analyze_row_clever("?#?#?#?#?#?#?#?", (1, 3, 1, 6)), 1)
u.assert_equal(analyze_row_clever("????.#...#...", (4, 1, 1)), 1)
u.assert_equal(analyze_row_clever("????.######..#####.", (1, 6, 5)), 4)
u.assert_equal(analyze_row_clever("?###????????", (3, 2, 1)), 10)  # 10 arrangements


def first_part_clever(raw_input):
    result = 0
    for row in raw_input.strip().split("\n"):
        symbols, digits = row.split(" ")
        digits = tuple(int(c) for c in digits.split(","))
        result += analyze_row_clever(symbols, digits)
    return result


# u.assert_equal(first_part_clever(ex_1),21)
