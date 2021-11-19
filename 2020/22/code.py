from itertools import count
from collections import deque
import random

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

COLORS = (u.RED, u.GREEN, u.YELLOW, u.PURPLE, u.CYAN, u.PINK)


def extract_decks_from_raw_input(input: str):
    deck1, deck2 = input.split("\n\n")
    deck1 = deque(map(int, deck1.splitlines()[1:]))
    deck2 = deque(map(int, deck2.splitlines()[1:]))
    return deck1, deck2


the_game_number = 0


def get_game_number():
    global the_game_number
    the_game_number += 1
    number = the_game_number
    color = random.choice(COLORS)
    return f"{color}{number}{u.NORMAL}"


def play_recursive_combat(deck1: deque, deck2: deque, level):
    pad = " " * level
    game_number = get_game_number()
    print(f"{pad}[{game_number}] BEGIN")
    already_seen1 = set()
    already_seen2 = set()
    for turn in count():
        config1 = tuple(deck1)
        config2 = tuple(deck2)
        if config1 in already_seen1 or config2 in already_seen2:
            print(
                f"{pad}[{game_number}] P1 WINS at turn {turn} by anti-infinite-protection"
            )
            return 1, deck1
        else:
            already_seen1.add(config1)
            already_seen2.add(config2)

        try:
            card1 = deck1.popleft()
        except IndexError:
            print(f"{pad}[{game_number}] P2 WINS at turn {turn}")
            return 2, deck2

        try:
            card2 = deck2.popleft()
        except IndexError:
            print(f"{pad}[{game_number}] P1 WINS at turn {turn}")
            return 1, deck1

        if card1 <= len(deck1) and card2 <= len(deck2):
            # launch a recursive combat
            sub_deck_1 = deque(list(deck1)[:card1])  # pick only the <card1> first cards
            sub_deck_2 = deque(list(deck2)[:card2])  # pick only the <card2> first cards
            winner, _ = play_recursive_combat(sub_deck_1, sub_deck_2, level + 1)
        elif card1 > card2:
            winner = 1
        elif card2 > card1:
            winner = 2

        if winner == 1:
            winner_deck = deck1
            winner_card = card1
            loser_card = card2
        else:
            winner_deck = deck2
            winner_card = card2
            loser_card = card1
        winner_deck.append(winner_card)
        winner_deck.append(loser_card)
        # print(deck1, deck2)


winner, deck = play_recursive_combat(*extract_decks_from_raw_input(example_input), 0)
u.assert_equals(count_points(deck), 291)

deck1, deck2 = extract_decks_from_raw_input(
    """Player 1:
43
19

Player 2:
2
29
14"""
)
play_recursive_combat(deck1, deck2, 0)

deck1, deck2 = extract_decks_from_raw_input(raw_input)
winner, deck = play_recursive_combat(deck1, deck2, 0)
u.answer_part_2(count_points(deck))
