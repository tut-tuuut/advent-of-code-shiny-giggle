import itertools
import utils as u

example_public_keys = (5764801, 17807724)

door_key = 1327981
card_key = 2822615

MODULO = 20201227
SUBJECT = 7

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def find_loop_size(public_key: int):
    value = 1
    for loop_size in itertools.count(start=1):
        value = (value * SUBJECT) % MODULO
        if value == public_key:
            return loop_size


def find_encryption_key(public_key: int, loop_size_of_other_device: int):
    encryption_key = 1
    for _ in range(loop_size_of_other_device):
        encryption_key = (encryption_key * public_key) % MODULO
    return encryption_key


u.assert_equals(find_loop_size(5764801), 8)
u.assert_equals(find_loop_size(17807724), 11)

u.assert_equals(find_encryption_key(5764801, 11), 14897079)

card_loop_size = find_loop_size(card_key)
u.pink(f"card loop: {card_loop_size}")
encryption_key = find_encryption_key(door_key, card_loop_size)

u.answer_part_1(encryption_key)
# 1018011 too low

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
