from math import lcm
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

second_example_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_raw_input(raw_input):
    instructions, network = raw_input.split("\n\n")
    net_dict = {}
    for row in network.strip().split("\n"):
        source = row[:3]
        left = row[7:10]
        right = row[12:15]
        net_dict[source] = (left, right)
    instructions = instructions.replace("L", "0").replace("R", "1")
    instructions = tuple(int(char) for char in instructions)
    return instructions, net_dict


parse_raw_input(example_input)


def part_1(input):
    instructions, network = parse_raw_input(input)
    step = "AAA"
    nb = 0
    l = len(instructions)
    while step != "ZZZ":
        step = network[step][instructions[nb % l]]
        nb += 1
    return nb


u.assert_equal(part_1(example_input), 2)
u.assert_equal(part_1(second_example_input), 6)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

part_2_example_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def part_2_dumb_and_slow(raw_input):
    instructions, network = parse_raw_input(raw_input)
    step = tuple(x for x in network.keys() if x[2] == "A")
    nb = 0
    l = len(instructions)
    while any(s[2] != "Z" for s in step):
        instruction = instructions[nb % l]
        step = tuple(network[k][instruction] for k in step)
        nb += 1
    return nb


u.assert_equal(part_2_dumb_and_slow(part_2_example_input), 6)


def part_2_fast(raw_input):
    instructions, network = parse_raw_input(raw_input)
    initial_steps = tuple(x for x in network.keys() if x[2] == "A")
    periods = dict()
    l = len(instructions)
    for step in initial_steps:
        nb = 0
        while step[2] != "Z":
            step = network[step][instructions[nb % l]]
            nb += 1
        periods[step] = nb

    return lcm(*periods.values())


u.assert_equal(part_2_fast(part_2_example_input), 6)

u.answer_part_2(part_2_fast(raw_input))
