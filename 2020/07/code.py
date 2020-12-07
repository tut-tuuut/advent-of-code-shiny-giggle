import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

container_pattern = re.compile(r"^(.*) bags? contain")
contained_pattern = re.compile(r"(\d+) (\w+ \w+) bags?")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# for rule in example_rules.splitlines():
#     container = container_pattern.match(rule).group(1)
#     contained = contained_pattern.findall(rule)
#     for number, color in contained:
#         print(f'"{container}" -> "{color}" [label={number}]')

for rule in raw_input.splitlines():
    container = container_pattern.match(rule).group(1)
    contained = contained_pattern.findall(rule)
    for number, color in contained:
        print(f'"{container}" -> "{color}" [label={number}]')


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
