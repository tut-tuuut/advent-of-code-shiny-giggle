import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def analyse_stream(raw_input):
    ignore_mode = False
    garbage_mode = False
    opened_groups = 0
    global_score = 0
    for char in raw_input:
        if ignore_mode:
            ignore_mode = False
            continue
        if garbage_mode:
            if char == ">":
                garbage_mode = False
            elif char == "!":
                ignore_mode = True
            continue
        if char == "{":
            opened_groups += 1
        elif char == "}":
            global_score += opened_groups
            opened_groups -= 1
        elif char == "<":
            garbage_mode = True
    return global_score


expected = {
    r"{}": 1,
    r"{{{}}}": 6,
    r"{{<!!>},{<!!>},{<!!>},{<!!>}}": 9,
}
for s, score in expected.items():
    u.assert_equals(analyse_stream(s), score)

u.answer_part_1(analyse_stream(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def count_garbage(raw_input):
    ignore_mode = False
    garbage_mode = False
    global_score = 0
    for char in raw_input:
        if ignore_mode:
            ignore_mode = False
            continue
        if garbage_mode:
            if char == ">":
                garbage_mode = False
            elif char == "!":
                ignore_mode = True
            else:
                global_score += 1
            continue
        if char == "<":
            garbage_mode = True
    return global_score


expected = {
    r"<>": 0,
    r"<random characters>": 17,
    r"<<<<>": 3,
    r"<{!>}>": 2,
    r"<!!>": 0,
    r"<!!!>>": 0,
    r'<{o"i!a,<{i<a>': 10,
}
for s, result in expected.items():
    u.assert_equals(count_garbage(s), result)

u.answer_part_2(count_garbage(raw_input))
