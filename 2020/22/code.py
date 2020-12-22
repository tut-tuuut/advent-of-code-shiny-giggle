from itertools import count
from collections import deque

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_winner_deck(input: str):
    deck1, deck2 = input.split("\n\n")
    deck1 = deque(map(int, deck1.splitlines()[1:]))
    deck2 = deque(map(int, deck2.splitlines()[1:]))
    for turn in count():
        try:
            card1 = deck1.popleft()
        except IndexError:
            print(f"player1 has lost after {turn} turns!")
            return deck2
        try:
            card2 = deck2.popleft()
        except IndexError:
            print(f"player2 has lost after {turn} turns!")
            return deck1
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)


def count_points(deck):
    return sum(idx * card for idx, card in enumerate(reversed(deck), start=1))


deck = get_winner_deck(example_input)
u.assert_equals(count_points(deck), 306)

deck = get_winner_deck(raw_input)
u.answer_part_1(count_points(deck))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
