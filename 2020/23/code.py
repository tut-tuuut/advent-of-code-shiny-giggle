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


def crab_moves_cups(labeling, rounds=10):
    cups = deque(map(int, list(labeling)))
    current = cups[0]
    for turn in range(rounds):
        current = cups.popleft()
        # The crab picks up the three cups that are immediately clockwise of the current cup.
        # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        picked = [cups.popleft() for _ in range(3)]
        cups.appendleft(current)
        # destination cup: the cup with a label equal to the current cup's label minus one.
        # If this would select one of the cups that was just picked up, the crab will keep
        # subtracting one until it finds a cup that wasn't just picked up.
        # If at any point in this process the value goes below the lowest value on any cup's label,
        # it wraps around to the highest value on any cup's label instead.
        destination = current - 1
        while destination not in cups:
            destination -= 1
            if destination < min(cups):
                destination = max(cups)
        # The crab places the cups it just picked up so that they are immediately clockwise
        # of the destination cup. They keep the same order as when they were picked up.
        destination_index = cups.index(destination)
        cups.rotate(
            5 - destination_index
        )  # this places the destination at the end of the deque
        cups.extend(picked)
        # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
        current_index = (cups.index(current) + 1) % 9
        cups.rotate(
            -current_index
        )  # this places the new current cup at the beginning of the deque
    debug_cups(cups, cups[0])
    return cups


crab_moves_cups(example_labeling)

cups_after_100_moves = crab_moves_cups(my_labeling, 100)
index_of_one = cups_after_100_moves.index(1)
cups_after_100_moves.rotate(-index_of_one)  # put 1 at the beginning of the deque
cups_after_100_moves.popleft()  # remove the one
u.answer_part_1("".join(map(str, cups_after_100_moves)))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
