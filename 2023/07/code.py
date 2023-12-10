import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read().strip()

example_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def hand_range(game):
    s = set(game)
    if len(s) == 5:  # all cards are different
        return 1
    if len(s) == 4:  # only one pair
        return 2
    if len(s) == 1:  # all cards are the same
        return 7
    counts = {game.count(card) for card in s}
    if len(s) == 3:
        if 3 in counts:
            return 4
        elif 2 in counts:
            return 3
    if len(s) == 2:
        if 4 in counts:
            return 6
        elif 3 in counts:
            return 5


u.assert_equal(hand_range("12345"), 1)
u.assert_equal(hand_range("A23A4"), 2)
u.assert_equal(hand_range("23432"), 3)
u.assert_equal(hand_range("TTT98"), 4)
u.assert_equal(hand_range("23332"), 5)
u.assert_equal(hand_range("AA8AA"), 6)
u.assert_equal(hand_range("66666"), 7)


# 23456789TJQKA
# 23456789BJQYZ
def part_1(raw_input):
    sortable_hands = {}
    for row in raw_input.strip().split("\n"):
        hand, bid = row.split(" ")
        sort_key = f"{hand_range(hand)}{hand.replace('A','Z').replace('T','B').replace('K', 'Y')}"
        sortable_hands[sort_key] = int(bid)
    return sum(
        (i + 1) * sortable_hands[key]
        for i, key in enumerate(sorted(sortable_hands.keys()))
    )


u.assert_equal(part_1(example_input), 6440)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
