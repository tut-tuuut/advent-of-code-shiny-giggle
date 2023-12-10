import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """A Y
B X
C Z"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
def score_of_round(raw_desc):
    other_played = raw_desc[0]
    i_played = raw_desc[2]
    # score for the shape you selected
    # (1 for Rock, 2 for Paper, and 3 for Scissors)
    score = {"X": 1, "Y": 2, "Z": 3}[i_played]

    # score for the outcome of the round
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).
    # i lost:
    if raw_desc in ("A Z", "B X", "C Y"):
        return score
    # draw:
    elif raw_desc in ("A X", "B Y", "C Z"):
        return score + 3
    # i win
    elif raw_desc in ("A Y", "B Z", "C X"):
        return score + 6
    else:
        u.red(f"OH OH {raw_desc}")


u.assert_equals(score_of_round("A Y"), 8)
u.assert_equals(score_of_round("B X"), 1)
u.assert_equals(score_of_round("C Z"), 6)


def score_of_given_input(raw_input):
    return sum(score_of_round(row) for row in raw_input.split("\n"))


u.assert_equals(score_of_given_input(example_input), 15)
u.answer_part_1(score_of_given_input(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

possibilities = "ABC"


def score_of_round_2(raw_desc):
    other_played = raw_desc[0]
    # A for Rock, B for Paper, and C for Scissors
    expected_output = raw_desc[2]
    # X lose, Y draw, Z win
    initial = possibilities.find(other_played)
    move = {"X": -1, "Y": 0, "Z": +1}[expected_output]
    i_play = possibilities[(initial + move) % 3]
    return {"A": 1, "B": 2, "C": 3}[i_play] + {"X": 0, "Y": 3, "Z": 6}[expected_output]


u.assert_equals(score_of_round_2("A Y"), 4)
u.assert_equals(score_of_round_2("B X"), 1)
u.assert_equals(score_of_round_2("C Z"), 7)

u.answer_part_2(sum(score_of_round_2(row) for row in raw_input.split("\n")))
