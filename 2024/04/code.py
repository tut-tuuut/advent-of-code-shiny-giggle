import utils as u
import itertools

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
example = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

ahr = """
X...
.M..
..A.
...S
..A.
.M..
X...
"""


def part_1(raw_str, needle="XMAS"):
    arr = tuple(raw_str.strip().splitlines())
    eldeen = needle[::-1]
    xmascount = 0
    # horiz ltr
    xmascount += sum(row.count(needle) for row in arr)
    # horiz rtl
    xmascount += sum(row.count(eldeen) for row in arr)
    # vertical bottom -> top
    for i, row in enumerate(arr):
        for j, char in enumerate(row):
            if char != needle[0]:
                continue
            try:
                if all(letter == arr[i + x][j] for x, letter in enumerate(needle)):
                    xmascount += 1
            except IndexError:
                pass
            try:
                if i >= 3 and all(
                    letter == arr[i - x][j] for x, letter in enumerate(needle)
                ):
                    xmascount += 1
            except IndexError:
                pass

            for dir_i, dir_j in itertools.product((1, -1), (1, -1)):
                try:
                    if (i + (len(needle) - 1) * dir_i < 0) or (
                        j + (len(needle) - 1) * dir_j < 0
                    ):
                        continue
                    if all(
                        letter == arr[i + x * dir_i][j + x * dir_j]
                        for x, letter in enumerate(needle)
                    ):
                        xmascount += 1
                except IndexError:
                    pass
    return xmascount


u.assert_equal(part_1(example), 18)
u.assert_equal(part_1(ahr), 2)

u.answer_part_1(part_1(raw_input))

# 2556 too high

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
