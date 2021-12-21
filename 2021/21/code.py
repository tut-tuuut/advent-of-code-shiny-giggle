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
def get_positions_and_scores(dice_history, starting_positions):
    if len(dice_history) == 0:
        return starting_positions, (0, 0)
    positions, scores = get_positions_and_scores(dice_history[:-1], starting_positions)
    die_value = dice_history[-1]
    player = (len(dice_history) - 1) % 2
    new_positions = list(positions)
    new_positions[player] = (new_positions[player] + die_value) % 10
    new_scores = list(scores)
    new_scores[player] += new_positions[player]
    if new_positions[player] == 0:
        new_scores[player] += 10
    return tuple(new_positions), tuple(new_scores)


def part_2(starting_position_one, starting_position_two):
    starting_positions = (starting_position_one, starting_position_two)
    to_explore = deque((value,) for value in frequencies.keys())
    winning_universes = [0, 0]
    while len(to_explore) > 0:
        to_try = to_explore.popleft()
        _, scores = get_positions_and_scores(to_try, starting_positions)
        if max(scores) < 21:
            for new_dice_value in frequencies.keys():
                to_explore.appendleft(to_try + (new_dice_value,))
        else:
            if scores[0] >= 21:
                winning_universes[0] += frequencies[to_try[-1]]
            elif scores[1] >= 21:
                winning_universes[1] += frequencies[to_try[-1]]
            print(sum(winning_universes), end="\r")
    return max(winning_universes)


u.assert_equals(part_2(4, 8), 444356092776315)
