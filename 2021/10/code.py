import utils as u
import statistics

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def clean_string(raw_input):
    l = None
    s = raw_input
    while l != len(s):
        l = len(s)
        s = s.replace("()", "").replace("{}", "").replace("<>", "").replace("[]", "")
    return s


def find_illegal_characters(raw_input):
    cleaned_input = clean_string(raw_input)
    illegals = "]>})"
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    found = []
    for row in cleaned_input.splitlines():
        indexes = [row.find(c) for c in illegals]
        if max(indexes) >= 0:
            found.append(row[min(i for i in indexes if i >= 0)])
    return sum(scores[c] for c in found)


u.assert_equals(find_illegal_characters(example_input), 26397)
u.answer_part_1(find_illegal_characters(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def find_closing_sequences(raw_input):
    cleaned_input = clean_string(raw_input)
    illegals = "]>})"
    legal_rows_reversed = [
        row[::-1]
        for row in cleaned_input.splitlines()
        if not any((i in row) for i in illegals)
    ]
    scores = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    all_row_scores = []
    for row in legal_rows_reversed:
        row_score = 0
        for c in row:
            row_score *= 5
            row_score += scores[c]
        all_row_scores.append(row_score)
    return statistics.median(all_row_scores)


u.assert_equals(find_closing_sequences(example_input), 288957)
u.answer_part_2(find_closing_sequences(raw_input))
