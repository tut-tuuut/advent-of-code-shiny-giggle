import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

grids = raw_input.split("\n\n")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def find_reflection(grid, debug=False):
    rows = grid.strip().split("\n")
    horiz = find_horiz_reflection(rows)
    if debug:
        print("\n".join("".join(row) for row in rows))
        print("\n\n")

    if horiz:
        return horiz
    transposed_rows = []
    for j in range(len(rows[0])):
        transposed_rows.append(tuple(row[j] for row in rows))
    if debug:
        print("\n".join("".join(row) for row in transposed_rows))
    return find_horiz_reflection(transposed_rows, factor=1)


def find_horiz_reflection(rows, debug=False, factor=100):
    height = len(rows)
    if debug:
        print("height : ", height)
    for i in range(height - 1):
        if debug:
            print("=======   analyzing row", i, "==========")
        for x in range(min(i + 1, height - i - 1)):
            if debug:
                print(rows[i - x])
            if debug:
                print(rows[i + x + 1])
            if debug:
                if rows[i - x] == rows[i + x + 1]:
                    print("oho :)")
                else:
                    print("nequal")
        if all(
            rows[i - x] == rows[i + x + 1] for x in range(min(i + 1, height - i - 1))
        ):
            if debug:
                print(i, "is a symmetry")
            return (i + 1) * factor


u.assert_equal(
    find_reflection(
        """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
    ),
    400,
)


u.assert_equal(
    find_reflection(
        """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
    ),
    5,
)


def part_1(raw_input):
    grids = raw_input.strip().split("\n\n")
    return sum(find_reflection(grid) for grid in grids)


u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
