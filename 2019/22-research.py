import re


def pick_one_in_increment(deck, increment):
    """This reverses a deck shuffled with the "deal with increment N" technique"""
    # 012301230123
    # *--*--*--*   => 0321
    return [deck[i * increment % len(deck)] for i in range(len(deck))]
    # I suppose it can work only if gcd(len(deck), increment) == 1


for i in range(2, 19):
    deck = list(range(19))
    deck = pick_one_in_increment(deck, i)
    print(i, [deck.index(z) for z in range(19)])

# https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbwauzi/?utm_source=reddit&utm_medium=web2x&context=3
# https://github.com/sasa1977/aoc/blob/master/lib/2019/201922.ex
# https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbtugcu/?utm_source=reddit&utm_medium=web2x&context=3