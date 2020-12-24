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
        tiling[(row, col)] *= -1
    return tiling


tiling = extract_black_tiles(example)
u.assert_equals(list(tiling.values()).count(-1), 10)

tiling = extract_black_tiles(raw_input)
u.answer_part_1(list(tiling.values()).count(-1))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
