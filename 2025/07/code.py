import utils as u
import re

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

def part_1(given_input):
    rays = set()
    division_count = 0
    for row in given_input.splitlines():
        if "S" in row:
            rays.add(row.find("S"))
        new_rays = rays.copy()
        for m in re.finditer("\^", row):
            divider_position = m.start()
            if divider_position in rays:
                new_rays.remove(divider_position)
                new_rays.add(divider_position - 1)
                new_rays.add(divider_position + 1)
                division_count = division_count + 1
        rays = new_rays
    return division_count

u.assert_equal(part_1(example), 21)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

"""
.......S.......
.......|.......
......|^|...... 2
......|.|......
.....|^|^|..... 2
.....|.|.|.....
....|^|^|^|.... 2
....|.|.|.|....
...|^|^|||^|... 5
...|.|.|||.|...
..|^|^|||^|^|.. 6
..|.|.|||.|.|..
.|^|||^||.||^|. 6
.|.|||.||.||.|.
|^|^|^|^|^|||^| 8
|.|.|.|.|.|||.|
"""