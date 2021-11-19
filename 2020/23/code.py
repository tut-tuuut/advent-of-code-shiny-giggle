import time
from collections import deque, defaultdict
import utils as u

example_labeling = "389125467"

my_labeling = "326519478"

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def debug_cups(cups: list, current: int):
    for cup in cups:
        if cup == current:
            print(f"{u.YELLOW}{cup}{u.NORMAL}", end=" ")
        else:
            print(cup, end=" ")
    print("")


def crab_moves_cups(cups: deque, rounds=10):
    current = cups[0]
    mini = min(cups)
    maxi = max(cups)
    l = len(cups)
    init_time = time.time()
    for turn in range(rounds):
        if turn % 500 == 0:
            duration = time.time() - init_time
        current = cups.popleft()
        picked = [cups.popleft() for _ in range(3)]
        cups.appendleft(current)
        destination = current - 1
        while destination in picked or destination < mini:
            destination -= 1
            if destination < mini:
                destination = maxi
        # THIS is slow: searching a value in a deque
        destination_index = cups.index(destination) + 1
        for add in reversed(picked):
            cups.insert(destination_index, add)
        # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
        cups.rotate(-1)  # this places the new current cup at the beginning of the deque
    return cups


example_cups = deque(map(int, list(example_labeling)))
example_cups = crab_moves_cups(example_cups)
u.assert_equals("".join(map(str, example_cups)), "837419265")


my_cups = deque(map(int, list(my_labeling)))
cups_after_100_moves = crab_moves_cups(my_cups, 100)
index_of_one = cups_after_100_moves.index(1)
cups_after_100_moves.rotate(-index_of_one)  # put 1 at the beginning of the deque
cups_after_100_moves.popleft()  # remove the one
answer_part_1 = "".join(map(str, cups_after_100_moves))

u.assert_equals(answer_part_1, "25368479")
u.answer_part_1(answer_part_1)

# # part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def build_chained_list(seed: str, length: int):
    """instead of storing every cup in order, store every cup with the label of the
    next cup in the circle"""
    d = dict()
    seed = list(map(int, list(seed)))
    current = seed[0]
    for i, value in enumerate(seed[:-1]):
        d[value] = seed[i + 1]
    if length > len(seed):
        # last cup of the seed is next to the first "extension" cup
        d[seed[-1]] = len(seed) + 1
        # then, extend to have a long enough dict
        d.update({i: i + 1 for i in range(len(seed) + 1, length)})
        # and close the circle
        d[length] = current
    else:
        d[seed[-1]] = current
    return d


def debug_chained_list(cups: dict, current: int):
    print(f"{u.YELLOW}{current}{u.NORMAL}", end=" ")
    for _ in range(len(cups) - 1):
        current = cups[current]
        print(current, end=" ")
    print("")


def cups_to_str(cups: list, begin=1):
    numbers = []
    current = begin
    for _ in range(len(cups)):
        numbers.append(str(current))
        current = cups[current]
    return "".join(numbers)


def crab_moves_cups_but_faster(cups: dict, current, rounds=10):
    mini = 1
    maxi = max(cups.keys())
    for _ in range(rounds):
        # pick cups
        picked = (cups[current], cups[cups[current]], cups[cups[cups[current]]])
        # close circle after picking the cups
        cups[current] = cups[picked[2]]
        destination = current - 1
        while destination in picked or destination < mini:
            destination -= 1
            if destination < mini:
                destination = maxi
        destination_clockwise = cups[destination]
        cups[destination] = picked[0]
        cups[picked[2]] = destination_clockwise
        current = cups[current]
    return cups


example_chained_list = build_chained_list("389125467", 9)

new_chained_list = crab_moves_cups_but_faster(example_chained_list, 3, 10)

u.assert_equals(cups_to_str(new_chained_list, 8), "837419265")
u.blue("now try with bigger lists...")
example_BIG_list = build_chained_list("389125467", 1000000)
BIG_list_after_10M_moves = crab_moves_cups_but_faster(example_BIG_list, 3, 10000000)

u.assert_equals(BIG_list_after_10M_moves[1], 934001)
u.assert_equals(BIG_list_after_10M_moves[934001], 159792)

my_BIG_list = build_chained_list(my_labeling, 1000000)
my_list_after_10M_moves = crab_moves_cups_but_faster(
    my_BIG_list, int(my_labeling[0]), 10000000
)

clockwise_1st_position = my_list_after_10M_moves[1]
clockwise_2nd_position = my_list_after_10M_moves[clockwise_1st_position]

u.answer_part_2(clockwise_1st_position * clockwise_2nd_position)
