import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def rotate(l, steps):
    steps = steps % len(l)
    return l[steps:] + l[:steps]


u.assert_equals(rotate(list(range(5)), 2), [2, 3, 4, 0, 1])
u.assert_equals(rotate(list(range(5)), 7), [2, 3, 4, 0, 1])
u.assert_equals(rotate(list(range(5)), 5), list(range(5)))


def apply_lengths(list, lengths):
    total_rotation = 0
    for skip, length in enumerate(lengths):
        if length == len(list):
            list = list[::-1]
        elif length <= 1:
            list = list
        else:
            list = list[length - 1 :: -1] + list[length:]
        list = rotate(list, skip + length)
        total_rotation += skip + length
    return rotate(list, len(list) - (total_rotation % len(list)))


l = list(range(5))
u.assert_equals(apply_lengths(l, (3, 4, 1, 5)), [3, 4, 2, 1, 0])

l = list(range(256))
lengths = [int(x) for x in raw_input.split(",")]
l = apply_lengths(l, lengths)
u.answer_part_1(l[0] * l[1])
# 54990 too high


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
