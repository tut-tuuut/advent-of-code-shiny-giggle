import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_adapters = """16
10
15
5
1
11
7
19
6
12
4"""

second_example_adapters = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def plug_all_adapters_in_charging_outlet(raw_list_of_adapters_in_my_bag):
    joltages = list(map(int, raw_list_of_adapters_in_my_bag.splitlines()))
    joltages.append(0)  # the outlet
    joltages.append(max(joltages) + 3)  # the target
    joltages.sort()  # "make the chain"
    differences = [joltages[i + 1] - joltages[i] for i in range(len(joltages) - 1)]
    return differences.count(1) * differences.count(3)


u.assert_equals(plug_all_adapters_in_charging_outlet(example_adapters), 35)
u.assert_equals(plug_all_adapters_in_charging_outlet(second_example_adapters), 220)

u.answer_part_1(plug_all_adapters_in_charging_outlet(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
