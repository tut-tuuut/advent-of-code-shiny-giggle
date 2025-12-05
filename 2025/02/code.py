import utils as u
from more_itertools import chunked

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def is_invalid_id(given_id):
    l = len(given_id)
    return given_id[: l // 2] == given_id[l // 2 :]


u.assert_equal(is_invalid_id("123123"), True)
u.assert_equal(is_invalid_id("12323"), False)
u.assert_equal(is_invalid_id("123451"), False)


def part_1(given_input):
    intervals = given_input.split(",")
    nb_of_invalid_ids = 0
    for interval in intervals:
        start, end = interval.split("-")
        nb_of_invalid_ids = nb_of_invalid_ids + sum(
            id if is_invalid_id(str(id)) else 0
            for id in range(int(start), int(end) + 1)
        )
    return nb_of_invalid_ids


u.assert_equal(part_1("222220-222224"), 222222)

# u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def is_invalid_id_for_part_2(given_id):
    l = len(given_id)
    for x in range(1, l):
        if l % x != 0:
            continue
        chunks = list(chunked(given_id, x))
        str_chunks = set("".join(chunk) for chunk in chunks)
        if len(str_chunks) == 1:
            return True
    return False


u.assert_equal(is_invalid_id_for_part_2("121212"), True)
u.assert_equal(is_invalid_id_for_part_2("121112"), False)


def part_2(given_input):
    intervals = given_input.split(",")
    nb_of_invalid_ids = 0
    for interval in intervals:
        start, end = interval.split("-")
        nb_of_invalid_ids = nb_of_invalid_ids + sum(
            id if is_invalid_id_for_part_2(str(id)) else 0
            for id in range(int(start), int(end) + 1)
        )
    return nb_of_invalid_ids


u.answer_part_2(part_2(raw_input))
