import utils as u
from collections import deque
from functools import cache

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


def debug_explored(dict_explored):
    for dice, status in dict_explored.items():
        u.yellow("-".join(str(d) for d in dice))
        positions, scores = status
        print(f"positions :", positions)
        print(f"scores :", scores)


# Number of times each score arises from 3 throws.
frequencies = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
u.assert_equals(sum(frequencies.values()), 3 * 3 * 3)


@cache
def get_winning_outcomes(p1, p2, s1, s2, player):
    w1 = w2 = 0
    if player == 1:
        for dice_result, frequency in frequencies.items():
            new_p1 = (p1 + dice_result) % 10
            new_s1 = s1 + new_p1
            if new_p1 == 0:
                new_s1 += 10
            if new_s1 >= 21:
                w1 += frequency
            else:
                plus_w1, plus_w2 = get_winning_outcomes(new_p1, p2, new_s1, s2, 2)
                w1 += plus_w1 * frequency
                w2 += plus_w2 * frequency
    elif player == 2:
        for dice_result, frequency in frequencies.items():
            new_p2 = (p2 + dice_result) % 10
            new_s2 = s2 + new_p2
            if new_p2 == 0:
                new_s2 += 10
            if new_s2 >= 21:
                w2 += frequency
            else:
                plus_w1, plus_w2 = get_winning_outcomes(p1, new_p2, s1, new_s2, 1)
                w1 += plus_w1 * frequency
                w2 += plus_w2 * frequency
    return w1, w2


def part_2(starting_position_one, starting_position_two):
    return max(
        get_winning_outcomes(starting_position_one, starting_position_two, 0, 0, 1)
    )


u.assert_equals(get_winning_outcomes(4, 8, 0, 0, 1), (444356092776315, 341960390180808))
u.answer_part_2(part_2(8, 7))
