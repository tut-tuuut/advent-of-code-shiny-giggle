import utils as u
from collections import deque
from itertools import count
from time import time

puzzle_input = "077201"

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def debug_position(scores: list, positions: list):
    for idx, score in enumerate(scores):
        if idx == positions[0]:
            print(f"{u.CYAN}{score}{u.NORMAL}", end="")
        elif idx == positions[1]:
            print(f"{u.PINK}{score}{u.NORMAL}", end="")
        else:
            print(score, end="")
    print("")


def look_for_ten_recipes_after_nth(n: int):
    score = deque([3, 7])
    elves_position = [0, 1]
    # debug_position(score, elves_position)
    while True:
        new_scores = sum(score[pos] for pos in elves_position)
        score.extend(map(int, list(str(new_scores))))
        elves_position = [(pos + score[pos] + 1) % len(score) for pos in elves_position]
        # debug_position(score, elves_position)
        if len(score) >= n + 10:
            break
    return "".join(map(str, (score[x] for x in range(n, n + 10))))


u.assert_equals(look_for_ten_recipes_after_nth(9), "5158916779")
u.assert_equals(look_for_ten_recipes_after_nth(5), "0124515891")
u.assert_equals(look_for_ten_recipes_after_nth(2018), "5941429882")
u.assert_equals(look_for_ten_recipes_after_nth(18), "9251071085")

u.answer_part_1(look_for_ten_recipes_after_nth(int(puzzle_input)))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def look_for_pattern_in_recipes(pattern: str):
    score = "37"
    elves_position = [0, 1]
    init = time()
    for i in count():
        if i % 10000 == 0:
            print(f"round {i} - len = {len(score)} - time = {time() - init}", end="\r")
        new_scores = str(sum(int(score[pos]) for pos in elves_position))
        score += new_scores
        elves_position = [
            (pos + int(score[pos]) + 1) % len(score) for pos in elves_position
        ]
        if pattern in score[-7:]:
            print(f"round {i} - len = {len(score)} - time = {time() - init}")
            return score.index(pattern)


u.assert_equals(look_for_pattern_in_recipes("51589"), 9)
u.assert_equals(look_for_pattern_in_recipes("01245"), 5)
u.assert_equals(look_for_pattern_in_recipes("92510"), 18)
u.assert_equals(look_for_pattern_in_recipes("59414"), 2018)

u.answer_part_2(look_for_pattern_in_recipes(puzzle_input))
