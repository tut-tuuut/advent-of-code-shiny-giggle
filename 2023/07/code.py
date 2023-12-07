import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

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
    if len(s) == 1:  # all cards are the same
        return 7


u.assert_equal(hand_range("12345"), 1)
u.assert_equal(hand_range("A23A4"), 2)
u.assert_equal(hand_range("23432"), 3)
u.assert_equal(hand_range("TTT98"), 4)
u.assert_equal(hand_range("23332"), 5)
u.assert_equal(hand_range("AA8AA"), 6)
u.assert_equal(hand_range("66666"), 7)
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
