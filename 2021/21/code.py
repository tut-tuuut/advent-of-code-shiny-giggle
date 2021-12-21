import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_1(starting_position_one, starting_position_two):
    positions = [starting_position_one, starting_position_two]
    scores = [0, 0]
    die = 0
    die_launched = 0
    while max(scores) < 1000:
        for player in (0, 1):
            for _ in range(3):
                die = max(1, (die + 1) % 101)
                die_launched += 1
                positions[player] = (positions[player] + die) % 10
            scores[player] += positions[player]
            if positions[player] == 0:
                scores[player] += 10
            if scores[player] >= 1000:
                return die_launched * min(scores)
    return die_launched * min(scores)


u.assert_equals(part_1(4, 8), 739785)
u.answer_part_1(part_1(8, 7))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
