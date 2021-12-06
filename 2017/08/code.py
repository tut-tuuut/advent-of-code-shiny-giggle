from networkx.algorithms.centrality import group
import utils as u
from collections import defaultdict
import re

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def interpret_condition(group_slice, registries):
    registry, condition, value = group_slice
    value = int(value)
    if condition == ">":
        return registries[registry] > value
    elif condition == "<":
        return registries[registry] < value
    elif condition == ">=":
        return registries[registry] >= value
    elif condition == "<=":
        return registries[registry] <= value
    elif condition == "!=":
        return registries[registry] != value
    elif condition == "==":
        return registries[registry] == value
    print("aaaahhh")
    print(group_slice)


def interpret_instructions(raw_input):
    reg = re.compile(r"([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) ([<>=!]+) (-?\d+)")
    registries = defaultdict(lambda: 0)
    for row in raw_input.splitlines():
        m = reg.match(row)
        groups = m.groups()
        if interpret_condition(groups[3:], registries):
            registry, action, value = groups[:3]
            if action == "dec":
                registries[registry] -= int(value)
            elif action == "inc":
                registries[registry] += int(value)
    return max(registries.values())


u.assert_equals(interpret_instructions(example), 1)
u.answer_part_1(interpret_instructions(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def interpret_instructions_part_2(raw_input):
    reg = re.compile(r"([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) ([<>=!]+) (-?\d+)")
    registries = defaultdict(lambda: 0)
    max_ever = 0
    for row in raw_input.splitlines():
        m = reg.match(row)
        groups = m.groups()
        if interpret_condition(groups[3:], registries):
            registry, action, value = groups[:3]
            if action == "dec":
                registries[registry] -= int(value)
            elif action == "inc":
                registries[registry] += int(value)
            if registries[registry] > max_ever:
                max_ever = registries[registry]
    return max_ever


u.assert_equals(interpret_instructions_part_2(example), 10)
u.answer_part_2(interpret_instructions_part_2(raw_input))
