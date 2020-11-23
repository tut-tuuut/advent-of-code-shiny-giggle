import string
import re

santa_current_password = 'cqjxjnds'

LETTERS = string.ascii_lowercase
TRIPLETS = {string.ascii_lowercase[i:i+3] for i in range(24)}

def increment_password(password):
    lastLetter = password[-1:]
    if lastLetter == 'z' and len(password) > 1:
        return f'{increment_password(password[:-1])}a'
    elif lastLetter == 'z' and len(password) == 1:
        return 'za'
    else:
        return f'{password[:-1]}{chr(ord(lastLetter) + 1)}'


def first_criteria(password):
    # Passwords must include one increasing straight of at least three LETTERS,
    # like abc, bcd, cde, and so on, up to xyz.
    # They cannot skip LETTERS; abd doesn't count.
    for triplet in TRIPLETS:
        if triplet in password:
            return True
    return False

def second_criteria(password):
    # Passwords may not contain the LETTERS i, o, or l
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    return True

def third_criteria(password):
    # Passwords must contain at least two different,
    # non-overlapping pairs of LETTERS, like aa, bb, or zz.
    regex = r'([a-z])\1{1}'
    re.match(regex, password)
    return True

def is_good_password(password):
    return second_criteria(password) and third_criteria(password) and first_criteria(password)
# ----------

def find_next_good_password(password):
    for i in range(100):
        password = increment_password(password)
        if is_good_password(password):
            return password
    return 'not found in given limit'

# ----

"""
print(f'this should be abd: {increment_password("abc")}')
print(f'this should be aca: {increment_password("abz")}')
print(f'this should be caa: {increment_password("bzz")}')
print(f'this should be caaa: {increment_password("bzzz")}')
"""

print(f'this should be abcdffaa : {find_next_good_password("abcdefgh")}')