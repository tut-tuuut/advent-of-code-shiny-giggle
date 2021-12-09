import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def sum_risk_levels_of_low_points(raw_input):
    grid = tuple(tuple(int(x) for x in row) for row in raw_input.splitlines())
    low_points = extract_low_points(grid)
    return sum(grid[r][c] for r, c in low_points) + len(low_points)


def extract_low_points(grid):
    # inside the grid:
    low_points = [
        (row_number, col_number)
        for row_number in range(1, len(grid) - 1)
        for col_number in range(1, len(grid[0]) - 1)
        if all(
            grid[row_number][col_number] < x
            for x in (
                grid[row_number - 1][col_number],
                grid[row_number + 1][col_number],
                grid[row_number][col_number - 1],
                grid[row_number][col_number + 1],
            )
        )
    ]
    # top left corner
    if all(grid[0][0] < x for x in (grid[0][1], grid[1][0])):
        low_points.append((0, 0))
    # top right corner
    if all(grid[0][-1] < x for x in (grid[0][-2], grid[1][-1])):
        low_points.append((0, len(grid[0]) - 1))
    # bottom left corner
    if all(grid[-1][0] < x for x in (grid[-1][1], grid[-2][0])):
        low_points.append((len(grid) - 1, 0))
    # bottom right corner
    if all(grid[-1][-1] < x for x in (grid[-1][-2], grid[-2][-1])):
        low_points.append((len(grid) - 1, len(grid[0]) - 1))

    # top row excluding corners
    low_points.extend(
        (0, col_number)
        for col_number in range(1, len(grid[0]) - 1)
        if all(
            grid[0][col_number] < x
            for x in (
                grid[0][col_number - 1],
                grid[0][col_number + 1],
                grid[1][col_number],
            )
        )
    )

    # bottom row excluding corners
    low_points.extend(
        (len(grid) - 1, col_number)
        for col_number in range(1, len(grid[0]) - 1)
        if all(
            grid[-1][col_number] < x
            for x in (
                grid[-1][col_number - 1],
                grid[-1][col_number + 1],
                grid[-2][col_number],
            )
        )
    )
    # first column excluding corners
    low_points.extend(
        (row_number, 0)
        for row_number in range(1, len(grid) - 1)
        if all(
            grid[row_number][0] < x
            for x in (
                grid[row_number - 1][0],
                grid[row_number + 1][0],
                grid[row_number][1],
            )
        )
    )
    # last column excluding corners
    low_points.extend(
        (row_number, len(grid[0]) - 1)
        for row_number in range(1, len(grid) - 1)
        if all(
            grid[row_number][-1] < x
            for x in (
                grid[row_number - 1][-1],
                grid[row_number + 1][-1],
                grid[row_number][-2],
            )
        )
    )

    return low_points


u.assert_equals(sum_risk_levels_of_low_points(example_input), 15)


u.answer_part_1(sum_risk_levels_of_low_points(raw_input))

# 613 : too high

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def find_bassins(grid):
    low_points = extract_low_points(grid)
    width = len(grid[0])
    height = len(grid)
    bassins = []
    for low_point in low_points:
        to_check = [low_point]
        checked = []
        bassin = []
        while len(to_check) > 0:
            r, c = to_check.pop(0)
            if (r, c) in checked:
                continue
            if any(
                (
                    r >= height,  # ⎫
                    r < 0,  # ⎬ off grid
                    c >= width,  # ⎪
                    c < 0,  # ⎭
                )
            ):
                continue
            checked.append((r, c))
            if grid[r][c] == 9:  # bassin limit
                continue
            bassin.append((r, c))
            to_check.extend(
                (
                    (r + 1, c),
                    (r - 1, c),
                    (r, c - 1),
                    (r, c + 1),
                )
            )

        bassins.append(bassin)
    return bassins


def multiply_size_of_three_largest_bassins(raw_input):
    grid = tuple(tuple(int(x) for x in row) for row in raw_input.splitlines())
    bassins = find_bassins(grid)
    sizes = sorted([len(b) for b in bassins], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


u.assert_equals(multiply_size_of_three_largest_bassins(example_input), 1134)
u.answer_part_2(multiply_size_of_three_largest_bassins(raw_input))
