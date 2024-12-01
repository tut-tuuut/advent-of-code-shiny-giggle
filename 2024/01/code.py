import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example = """3   4
4   3
2   5
1   3
3   9
3   3"""


def extract_lists_from_raw_input(raw_input):
    llist = []
    rlist = []
    for row in raw_input.splitlines():
        if not row:
            continue
        left, right = row.split("   ")
        llist.append(int(left))
        rlist.append(int(right))
    return llist, rlist


def distance_between_two_lists(raw_input):
    left, right = extract_lists_from_raw_input(raw_input)
    left = sorted(left)
    right = sorted(right)
    return sum(abs(lid - rid) for lid, rid in zip(left, right))


u.assert_equal(distance_between_two_lists(example), 11)

u.answer_part_1(distance_between_two_lists(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def similarity_score(raw_input):
    left, right = extract_lists_from_raw_input(raw_input)
    right = tuple(sorted(right))
    return sum(left_el * right.count(left_el) for left_el in left)


u.assert_equal(similarity_score(example), 31)

u.answer_part_2(similarity_score(raw_input))
