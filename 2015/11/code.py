import string
import re
import utils as u

santa_current_password = 'cqjxjnds'

LETTERS = string.ascii_lowercase
TRIPLETS = {string.ascii_lowercase[i:i+3] for i in range(24)}

def increment_password(password):
    lastLetter = password[-1:]
    if lastLetter == 'z' and len(password) > 1:
        return f'{increment_password(password[:-1])}a'
    elif lastLetter == 'z' and len(password) == 1:
        return 'aa'
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

def fix_second_criteria(password, letter):
    if not letter in password:
        return password
    pos = password.find(letter)
    nextLetter = chr(ord(letter) + 1)
    return password[:pos] + nextLetter + 'a' * (len(password) - pos - 1)

def third_criteria(password):
    # Passwords must contain at least two different,
    # non-overlapping pairs of LETTERS, like aa, bb, or zz.
    regex = r'([a-z])\1{1}[a-z]*([a-z])\2{1}'
    if re.search(regex, password):
        return True
    return False

def is_good_password(password):
    return second_criteria(password) and third_criteria(password) and first_criteria(password)
# ----------

def find_next_good_password(password):
    for i in range(1000000):
        password = increment_password(password)
        
        if not second_criteria(password):
            password = fix_second_criteria(password, 'i')
            password = fix_second_criteria(password, 'o')
            password = fix_second_criteria(password, 'l')

        if not third_criteria(password):
            continue
        if not first_criteria(password):
            continue
        print(f'found in {i+1} iterations!')
        return password
    return 'not found in given limit'

# ----

u.assert_equals('abd', increment_password('abc'), "increment_password('abc')")
u.assert_equals('abe', increment_password('abc'), "increment_password('abc')")

u.assert_equals('abd', increment_password("abc"), "increment_password abc")
u.assert_equals('aca', increment_password("abz"), "increment_password abz")
u.assert_equals('caa', increment_password("bzz"), "increment_password bzz")
u.assert_equals('caaa', increment_password("bzzz"), "increment_password bzzz")
u.assert_equals('xy', increment_password("xx"), "increment_password xx")

u.assert_equals(True, first_criteria('abcdffaa'))
u.assert_equals(True, second_criteria('abcdffaa'))
u.assert_equals(True, third_criteria('abcdffaa'))

u.assert_equals(fix_second_criteria('abciabc', 'i'), 'abcjaaa')
u.assert_equals('abcdffaa', find_next_good_password("abcdefgh"))
u.assert_equals('ghjaabcc', find_next_good_password("ghijklmn"))

part1 = find_next_good_password(santa_current_password)
u.answer_part_1(part1)

u.answer_part_2(find_next_good_password(part1))