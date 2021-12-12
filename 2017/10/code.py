import utils as u
from operator import xor
from functools import reduce


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


def part_2(raw_input):
    lengths = [ord(char) for char in raw_input] + [17, 31, 73, 47, 23]
    print(lengths)
    sparse_hash = apply_lengths(list(range(255)), lengths * 64)
    dense_hash = [reduce(xor, sparse_hash[sl * 16 : sl * 16 + 16]) for sl in range(16)]
    return "".join(hex(number)[2:] for number in dense_hash)


tests = {
    "": "a2582a3a0e66e6e86e3812dcb672a272",
    "AoC 2017": "33efeb34ea91902bb2f59c9920caa6cd",
    "1,2,3": "3efbe78a8d82f29979031a4aa0b16a9d",
    "1,2,4": "63960835bcdc130f0b66d7ff4f6a5a8e",
}
for input, expected in tests.items():
    u.assert_equals(part_2(input), expected)

u.answer_part_2(part_2(raw_input))

# d9c222bce5a518a393d3278dbcbeae7 : nope
