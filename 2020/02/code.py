import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    input_str = file.read()

regex = re.compile(r"(?P<from>\d+)-(?P<to>\d+)\s(?P<letter>\w):\s(?P<password>\w+)")


def is_valid_password(input_str):
    nb_from, nb_to, letter, password = regex.search(input_str).groups()
    return int(nb_from) <= password.count(letter) <= int(nb_to)


def is_valid_password_for_part_two(input_str):
    nb_from, nb_to, letter, password = regex.search(input_str).groups()
    return (password[int(nb_from) - 1], password[int(nb_to) - 1]).count(letter) == 1


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.assert_equals(is_valid_password("1-3 a: abcde"), True)
u.assert_equals(is_valid_password("1-3 b: cdefg"), False)
u.assert_equals(is_valid_password("2-9 c: ccccccccc"), True)

u.answer_part_1(sum(1 for string in input_str.split("\n") if is_valid_password(string)))
# 347 too low
# 519 OK

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.assert_equals(is_valid_password_for_part_two("1-3 a: abcde"), True)
u.assert_equals(is_valid_password_for_part_two("1-3 b: cdefg"), False)
u.assert_equals(is_valid_password_for_part_two("2-9 c: ccccccccc"), False)

u.answer_part_2(
    sum(1 for string in input_str.split("\n") if is_valid_password_for_part_two(string))
)
