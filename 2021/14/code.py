from more_itertools import windowed
from collections import defaultdict

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_1(raw_input, steps=10):
    pairs = {}
    initial = ""
    for row in filter(None, raw_input.splitlines()):
        if "->" in row:
            source, new = row.split(" -> ")
            pairs[source] = f"{source[0]}{new}"
        elif row:
            initial = row
    cur_string = initial
    for _ in range(steps):
        new_string = (
            "".join(
                pairs.get(pair) if pair in pairs else pair[0]
                for pair in ("".join(t) for t in windowed(cur_string, 2))
            )
            + cur_string[-1]
        )
        cur_string = new_string
    counts = {letter: cur_string.count(letter) for letter in set(cur_string)}
    return max(counts.values()) - min(counts.values())


u.assert_equals(part_1(example), 1588)
u.answer_part_1(part_1(raw_input))


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
