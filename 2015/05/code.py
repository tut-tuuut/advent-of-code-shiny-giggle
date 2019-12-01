import re

def is_nice(s):
    if len(re.findall(r'[aeiou]', s)) < 3:
        return False
    if len(re.findall(r'(ab|cd|pq|xy)', s)) >= 1:
        return False
    for letter in s:
        if s.count(f'{letter}{letter}') > 0:
            return True
    return False

print(f'This should be True: {is_nice("ugknbfddgicrmopn")}')
print(f'This should be True: {is_nice("aaa")}')
print(f'This should be False: {is_nice("jchzalrnumimnmhp")}')
print(f'This should be False: {is_nice("haegwjzuvuyypxyu")}')
print(f'This should be False: {is_nice("dvszwmarrgswjxmb")}')