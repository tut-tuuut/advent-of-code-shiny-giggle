import re

with open(__file__ + ".input", "r+") as file:
    inputStr = file.read()


def is_nice(s):
    if len(re.findall(r"[aeiou]", s)) < 3:
        return False
    if len(re.findall(r"(ab|cd|pq|xy)", s)) >= 1:
        return False
    for letter in s:
        if s.count(f"{letter}{letter}") > 0:
            return True
    return False


# print(f'This should be True: {is_nice("ugknbfddgicrmopn")}')
# print(f'This should be True: {is_nice("aaa")}')
# print(f'This should be False: {is_nice("jchzalrnumimnmhp")}')
# print(f'This should be False: {is_nice("haegwjzuvuyypxyu")}')
# print(f'This should be False: {is_nice("dvszwmarrgswjxmb")}')

listOfStrings = inputStr.split("\n")
niceStrings = list(filter(is_nice, listOfStrings))
# print(f'PART1: there are {len(niceStrings)} nice strings.')


def is_nice_2nd(s):
    firstCondition = False
    secondCondition = False
    # Now, a nice string is one with all of the following properties:
    # It contains a pair of any two letters that appears at least twice in the string without overlapping,
    # like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    for i, l in enumerate(s):
        if i >= len(s) - 1:
            continue
        pair = s[i : i + 2]
        rest = s[i + 2 :]
        if rest.count(pair) > 0:
            firstCondition = True
            break

    for i, l in enumerate(s):
        if i >= len(s) - 2:
            break
        if l == s[i + 2]:
            secondCondition = True
            break

    return firstCondition and secondCondition

    # It contains at least one letter which repeats with exactly one letter between them,
    # like xyx, abcdefeghi (efe), or even aaa.


print(f'This should be True: {is_nice_2nd("qjhvhtzxzqqjkmpb")}')
print(f'This should be True: {is_nice_2nd("xxyxx")}')

print(f'This should be False: {is_nice_2nd("uurcxstgmygtbstg")}')
print(f'This should be False: {is_nice_2nd("ieodomkazucvgmuy")}')

#    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

niceStrings = list(filter(is_nice_2nd, listOfStrings))
print(f"PART2: there are {len(niceStrings)} nice strings.")
