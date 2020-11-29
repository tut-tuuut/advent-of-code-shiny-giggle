import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()


def does_sue_match_criteria_part_1(sue, criteria):
    for key in sue:
        if sue[key] != criteria[key]:
            return False
    return True


def does_sue_match_criteria_part_2(sue, criteria):
    for key in sue:
        # the cats and trees readings indicates that there are greater than that many
        if key in ("cats", "trees"):
            if sue[key] <= criteria[key]:
                return False
        # the pomeranians and goldfish readings indicate that there are fewer than that many
        elif key in ("pomeranians", "goldfish"):
            if sue[key] >= criteria[key]:
                return False
        elif sue[key] != criteria[key]:
            return False
    return True


criteria = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
parser = r"""Sue\s(\d+)\: # Sue number
\s(\w+)\:\s(\d+), # info 1
\s(\w+)\:\s(\d+), # info 2
\s(\w+)\:\s(\d+) # info 3
"""
pattern = re.compile(parser, re.X | re.M)


for group in pattern.findall(inputStr):
    sueNumber, carac1, nb1, carac2, nb2, carac3, nb3 = group
    sue = {carac1: int(nb1), carac2: int(nb2), carac3: int(nb3)}
    if does_sue_match_criteria_part_1(sue, criteria):
        u.answer_part_1(sueNumber)
    if does_sue_match_criteria_part_2(sue, criteria):
        u.answer_part_2(sueNumber)
