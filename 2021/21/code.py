import utils as u
from collections import deque

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


def part_2(starting_position_one, starting_position_two):
    positions = [starting_position_one, starting_position_two]
    explored = {(): ((starting_position_one, starting_position_two), (0, 0))}
    to_explore = deque([(1,), (2,), (3,)])
    winning_universes = [0, 0]
    while len(to_explore):
        to_try = to_explore.popleft()
        die_value = to_try[-1]
        positions, scores = explored[to_try[:-1]]
        player = ((len(to_try) - 1) // 3) % 2
        new_positions = list(positions)
        new_positions[player] = (new_positions[player] + die_value) % 10
        if len(to_try) % 3 == 0:
            new_scores = list(scores)
            new_scores[player] += new_positions[player]
            if new_positions[player] == 0:
                new_scores[player] += 10
        else:
            new_scores = scores
        if max(new_scores) < 21:
            explored[to_try] = (tuple(new_positions), tuple(new_scores))
            for new_dice_value in (1, 2, 3):
                to_explore.appendleft(to_try + (new_dice_value,))
        else:
            if new_scores[0] >= 21:
                winning_universes[0] += 1
            elif new_scores[1] >= 21:
                winning_universes[1] += 1
            print(sum(winning_universes), end="\r")
    return max(winning_universes)


u.assert_equals(part_2(4, 8), 444356092776315)
