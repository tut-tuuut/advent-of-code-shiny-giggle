import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.answer_part_1("allez")


def part_1(given_input):
    ranges_str, ids_str = given_input.split("\n\n")
    ranges = tuple(
        tuple(int(x) for x in row.split("-")) for row in ranges_str.splitlines()
    )
    ids = tuple(int(x) for x in ids_str.splitlines())
    number_of_fresh_ingredients = 0
    for id in ids:
        if any(low <= id <= top for low, top in ranges):
            number_of_fresh_ingredients = number_of_fresh_ingredients + 1
    return number_of_fresh_ingredients


u.assert_equal(part_1(example), 3)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def sort_key(input_tuple):
    return input_tuple[1] - input_tuple[0]


def merge_ranges(given_ranges):
    # take longer intervals first
    given_ranges = reversed(sorted(given_ranges, key=sort_key))
    merged_ranges = []
    for interval in given_ranges:
        low, top = interval
        copy_of_merged_ranges = merged_ranges.copy()
        for x, existing_ranges in enumerate(copy_of_merged_ranges):
            ex_low, ex_top = existing_ranges
            if ex_low <= low <= ex_top and ex_top <= top:
                merged_ranges[x] = (ex_low, top)
                break
            elif low <= ex_low and ex_low <= top <= ex_top:
                merged_ranges[x] = (low, ex_top)
                break
            if ex_low <= low <= top <= ex_top:
                break  # nothing to do
        else:  # no intersection with existing intervals
            merged_ranges.append((low, top))

        if len(merged_ranges) == 0:
            merged_ranges.append((low, top))
    return merged_ranges


def part_2(given_input):
    ranges_str, _ = given_input.split("\n\n")
    given_ranges = tuple(
        tuple(int(x) for x in row.split("-")) for row in ranges_str.splitlines()
    )
    len_before_merge = len(given_ranges)
    merged_ranges = merge_ranges(given_ranges)
    len_after_merge = len(merged_ranges)
    while len_after_merge < len_before_merge:
        len_before_merge = len_after_merge
        merged_ranges = merge_ranges(merged_ranges)
        len_after_merge = len(merged_ranges)
    return sum(1 + top - low for low, top in merged_ranges)


u.assert_equal(part_2(example), 14)

my_example = """1-3
3-6
7-10
11-20
2-7

78"""

u.assert_equal(part_2(my_example), 20)
u.answer_part_2(part_2(raw_input))

# 360881927228856 too high (did not take into account included intervals)
# 349966814727677 too high
# 345755049374932 good (just merged more until nothing is merged anymore :shrug:)
