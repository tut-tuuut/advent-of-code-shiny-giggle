import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

grids = raw_input.split("\n\n")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def find_reflection(grid, debug=False):
    rows = grid.strip().split("\n")
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
            return (i + 1) * 100


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
)


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

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
