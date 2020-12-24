import re
from collections import defaultdict

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

PATH_FINDER = re.compile(r"(?:s|n)?(?:e|w)")


def extract_black_tiles(path_descriptor: str):
    tiling = defaultdict(lambda: 1)  # 1 = white, -1 = black
    for path in path_descriptor.splitlines():
        row = 0
        col = 0
        for direction in PATH_FINDER.findall(path):
            if direction == "e":
                col += 2
            elif direction == "w":
                col -= 2
            elif direction == "sw":
                row += 1
                col -= 1
            elif direction == "nw":
                row -= 1
                col -= 1
            elif direction == "se":
                row += 1
                col += 1
            elif direction == "ne":
                row -= 1
                col += 1
            else:
                print("duh?")
        tiling[row, col] *= -1
    return tiling


def count_black_tiles(grid: dict):
    return list(grid.values()).count(-1)


example_tiling = extract_black_tiles(example)
u.assert_equals(count_black_tiles(example_tiling), 10)

tiling = extract_black_tiles(raw_input)
u.assert_equals(count_black_tiles(tiling), 317)

u.answer_part_1(count_black_tiles(tiling))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def count_black_neighbors(grid: defaultdict, coordinates: tuple):
    return [
        grid[coordinates] for coordinates in get_neighbors_coordinates(coordinates)
    ].count(-1)


def get_neighbors_coordinates(coordinates: tuple):
    row, col = coordinates
    neighbors_offsets = ((0, 2), (0, -2), (1, 1), (1, -1), (-1, -1), (-1, 1))
    for row_offset, col_offset in neighbors_offsets:
        yield row + row_offset, col + col_offset


def build_next_grid(grid):
    current_keys = set(grid.keys())
    next_keys = current_keys.copy()
    for tile in current_keys:
        for neighbor in get_neighbors_coordinates(tile):
            next_keys.add(neighbor)
    new_grid = defaultdict(lambda: 1)
    for key in next_keys:
        if grid[key] == -1:
            # it is black: turns white if zero or more than 2 black neighbors
            # so it stays black if 1 or 2 black neighbors
            if count_black_neighbors(grid, key) in (1, 2):
                new_grid[key] = -1
        elif grid[key] == 1:
            if count_black_neighbors(grid, key) == 2:
                new_grid[key] = -1
    return new_grid


tests = {
    1: 15,
    2: 12,
    3: 25,
    4: 14,
    5: 23,
    6: 28,
    7: 41,
    8: 37,
    9: 49,
    10: 37,
    20: 132,
    30: 259,
    40: 406,
    50: 566,
    60: 788,
    70: 1106,
    80: 1373,
    90: 1844,
    100: 2208,
}

for days in range(1, 101):
    example_tiling = build_next_grid(example_tiling)
    if days in tests:
        u.assert_equals(
            count_black_tiles(example_tiling),
            tests[days],
            f" black tiles after {days} days",
        )

for days in range(100):
    tiling = build_next_grid(tiling)

u.answer_part_2(count_black_tiles(tiling))
# 3822 too high because I did only 99 days DUH