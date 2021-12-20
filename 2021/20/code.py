import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_input(raw_input):
    lines = raw_input.splitlines()
    algorithm = lines.pop(0).replace("#", "1").replace(".", "0")
    lines = tuple(
        row.replace("#", "1").replace(".", "0") for row in filter(None, lines)
    )
    return algorithm, lines


def yield_9_pixels(row, column, grid, default="0"):
    width = len(grid[0])
    height = len(grid)
    for j in range(row - 1, row + 2):
        for i in range(column - 1, column + 2):
            if any((i < 0, j < 0, j >= height, i >= width)):
                yield default
            else:
                yield (grid[j][i])


def calculate_next_grid(lines, algorithm, default="0"):
    return [
        "".join(
            algorithm[int("".join(yield_9_pixels(row, col, lines, default=default)), 2)]
            for col in range(-3, len(lines[0]) + 3)
        )
        for row in range(-3, len(lines) + 3)
    ]


def part_1(raw_input):
    algorithm, lines = parse_input(raw_input)
    if algorithm[0] == "1":
        default_on_odd_turns = "1"
    else:
        default_on_odd_turns = "0"
    lines = calculate_next_grid(lines, algorithm, default="0")
    lines = calculate_next_grid(lines, algorithm, default=default_on_odd_turns)
    return sum(row.count("1") for row in lines)


u.assert_equals(part_1(example), 35)
u.answer_part_1(part_1(raw_input))  # 5464! YAY

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
