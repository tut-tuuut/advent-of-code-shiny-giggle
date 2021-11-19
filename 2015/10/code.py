inputStr = "3113322113"


def elvesSay(s):
    cursor = 0
    i = 1
    result = ""
    l = len(s)
    while cursor + i <= l:
        if cursor == l - 1:
            result = f"{result}1{s[cursor]}"
            break
        while cursor + i < l and s[cursor] == s[cursor + i]:
            i = i + 1
        result = f"{result}{i}{s[cursor]}"
        cursor = cursor + i
        i = 1
    return result


print(f'this should be 331211: {elvesSay("33321")}')
print(f'this should be 23111221: {elvesSay("331211")}')

print(f'this should be 132123222113: {elvesSay("3113322113")}')

for i in range(40):
    inputStr = elvesSay(inputStr)

part1_answer = len(inputStr)
print(f"part1 answer: {part1_answer}")  # 329356 good answer!

ratios = []
for i in range(6):
    print(f"calculating ratio {41 + i} / {40 + i}")
    newInputStr = elvesSay(inputStr)
    print(len(newInputStr) / len(inputStr))
    ratios.append(len(newInputStr) / len(inputStr))
    inputStr = newInputStr

medium_ratio = sum(ratios) / len(ratios)

part2_answer = part1_answer * medium_ratio ** 10

print(part2_answer)
# 4666952 too high
# 4665481
# 4663725 too low
# 3580111 too low
