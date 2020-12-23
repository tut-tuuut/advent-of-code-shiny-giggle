import time
from collections import deque
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
            print(f"{duration:.4} - turn {turn}")
        current = cups.popleft()
        print(f"current {current}")
        picked = [cups.popleft() for _ in range(3)]
        print(f"pick {picked}")
        cups.appendleft(current)
        destination = current - 1
        while destination in picked or destination < mini:
            destination -= 1
            if destination < mini:
                destination = maxi
        # THIS is slow: searching a value in a deque
        destination_index = cups.index(destination) + 1
        print(f"destination {destination} at idx {destination_index}")
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

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example_cups = deque(map(int, list(example_labeling)))
example_cups.extend(range(10, 101))

cups = crab_moves_cups(example_cups, 50)
