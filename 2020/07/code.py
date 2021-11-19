import re
import itertools

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

MY_BAG = "shiny gold"  # bling bling

container_pattern = re.compile(r"^(.*) bags? contain")
contained_pattern = re.compile(r"(\d+) (\w+ \w+) bags?")

raw_example_ruleset = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


# Analysis *'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# for rule in raw_example_ruleset.splitlines():
#     container = container_pattern.match(rule).group(1)
#     contained = contained_pattern.findall(rule)
#     for number, color in contained:
#         print(f'"{container}" -> "{color}" [label={number}]')

# for rule in raw_input.splitlines():
#     container = container_pattern.match(rule).group(1)
#     contained = contained_pattern.findall(rule)
#     for number, color in contained:
#         print(f'"{container}" -> "{color}" [label={number}]')

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_rules(ruleset):
    rules = {}
    for rule in ruleset.splitlines():
        container = container_pattern.match(rule).group(1)
        contained = contained_pattern.findall(rule)
        rules[container] = {color: int(qty) for qty, color in contained}
    return rules


def get_parent_colors(rules, color):
    parent_colors = [bag for bag, colors in rules.items() if color in colors]
    return set(parent_colors) | set(
        itertools.chain.from_iterable(
            [get_parent_colors(rules, parent) for parent in parent_colors]
        )
    )


example_ruleset = parse_rules(raw_example_ruleset)
u.assert_equals(len(get_parent_colors(example_ruleset, MY_BAG)), 4)

ruleset = parse_rules(raw_input)
u.answer_part_1(len(get_parent_colors(ruleset, MY_BAG)))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def calculate_luggage_cost(rules, color):
    return sum(
        qty + qty * calculate_luggage_cost(rules, child_color)
        for child_color, qty in rules[color].items()
    )


u.assert_equals(calculate_luggage_cost(example_ruleset, MY_BAG), 32)

another_example_raw_ruleset = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

another_example_ruleset = parse_rules(another_example_raw_ruleset)

u.assert_equals(calculate_luggage_cost(another_example_ruleset, MY_BAG), 126)

u.answer_part_2(calculate_luggage_cost(ruleset, MY_BAG))
