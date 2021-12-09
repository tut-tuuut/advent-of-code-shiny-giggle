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
