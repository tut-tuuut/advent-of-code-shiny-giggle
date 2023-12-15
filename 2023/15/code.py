import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def hash_string(str):
    current_value = 0
    for c in str:
        current_value += ord(c)
        current_value = (current_value * 17) % 256
    return current_value


u.assert_equal(hash_string("HASH"), 52)
u.assert_equal(hash_string("pc=6"), 214)


def part_1(raw_input):
    return sum(hash_string(str) for str in raw_input.strip().split(","))


u.assert_equal(part_1("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"), 1320)

u.answer_part_1(part_1(raw_input))

# 514435 too high, i needed to strip() my raw input first

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
