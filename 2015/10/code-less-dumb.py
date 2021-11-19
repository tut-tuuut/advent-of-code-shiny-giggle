import re

inputStr = "3113322113"


def elvesSay(s):
    # https://docs.python.org/3/library/re.html#re.sub
    regex = r"(\d)\1*"
    # (\d) one digit in capturing group,
    # \1* followed by O or more of the result of the 1st capturing group
    return re.sub(regex, lambda x: f"{len(x.group(0))}{x.group(1)}", s)


print(f'this should be 331211: {elvesSay("33321")}')
print(f'this should be 23111221: {elvesSay("331211")}')

print(f'this should be 132123222113: {elvesSay("3113322113")}')


for i in range(40):
    inputStr = elvesSay(inputStr)

part1_answer = len(inputStr)
print(f"part1 answer: {part1_answer}")  # 329356 good answer!

for i in range(10):
    inputStr = elvesSay(inputStr)

part2_answer = len(inputStr)

print(part2_answer)  # 4666278 good answer
# 4666952 too high
# 4665481
# 4663725 too low
# 3580111 too low
