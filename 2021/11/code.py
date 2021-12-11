import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_next_step(grid):
    new_grid = [[i + 1 for i in row] for row in grid]
    flashed = []
    flashing = []
    for i, row in enumerate(new_grid):
        for j, char in enumerate(row):
            if char > 9:
                flashing.append((i, j))
    while len(flashing) > 0:
        octopus = flashing.pop(0)
        if octopus in flashed:
            continue
        i, j = octopus
        for ni, nj in get_neighbors(i, j):
            new_grid[ni][nj] += 1
            if new_grid[ni][nj] > 9:
                flashing.append((ni, nj))
        flashed.append((i, j))
    for i, j in flashed:
        new_grid[i][j] = 0
    return new_grid, len(flashed)


def get_neighbors(i, j):
    if i > 0:
        yield (i - 1, j)
        if j > 0:
            yield (i - 1, j - 1)
        if j < 9:
            yield (i - 1, j + 1)
    if j > 0:
        yield (i, j - 1)
    if j < 9:
        yield (i, j + 1)
    if i < 9:
        yield (i + 1, j)
        if j > 0:
            yield (i + 1, j - 1)
        if j < 9:
            yield (i + 1, j + 1)


def debug_grid(grid, flashes):
    print(f"┌{'─'*len(grid[0])}┐")
    for i, row in enumerate(grid):
        print(
            "│"
            + "".join(
                u.yellow(val % 10, True)
                if (i, j) in flashes
                else u.purple(val % 10, True)
                for j, val in enumerate(row)
            )
            + "│"
        )
    print(f"└{'─'*len(grid[0])}┘")


def part_1(raw_input, steps):
    grid = [[int(c) for c in row] for row in raw_input.splitlines()]
    total_nb_of_flashes = 0
    for _ in range(steps):
        grid, flashes = get_next_step(grid)
        total_nb_of_flashes += flashes
    return total_nb_of_flashes


u.assert_equals(part_1(example_input, 10), 204)
u.assert_equals(part_1(example_input, 100), 1656)
u.answer_part_1(part_1(raw_input, 100))

other_example = """11111
19991
19191
19991
11111"""

# part_1(other_example,1)
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(raw_input):
    grid = [[int(c) for c in row] for row in raw_input.splitlines()]
    for step in range(1000):
        grid, flashes = get_next_step(grid)
        if flashes == 100:
            return step + 1


u.assert_equals(part_2(example_input), 195)
u.answer_part_2(part_2(raw_input))
