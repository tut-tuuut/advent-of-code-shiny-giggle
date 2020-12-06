import re

with open(__file__ + ".input") as file:
    raw_input = file.read()


def deal_into_new_stack(deck):
    deck.reverse()
    return deck


def cut(deck, number_of_cards):
    return deck[number_of_cards:] + deck[:number_of_cards]


def pick_one_in_increment(deck, increment):
    # First try: does not work exactly how it should
    # (= does not work)
    # 012301230123
    # *--*--*--*   => 0321
    return [deck[i * increment % len(deck)] for i in range(len(deck))]
    # I suppose it can work only if gcd(len(deck), increment) == 1


def deal_with_increment(deck, increment):
    # element list[i] is at index (i * increment % len) in the new deck
    new_deck = [None] * len(deck)
    for i in range(len(deck)):
        new_deck[i * increment % len(deck)] = deck[i]
    return new_deck


digit_pattern = re.compile(r"(-?\d+)")


def execute_instruction(deck, instruction):
    if "deal into" in instruction:
        return deal_into_new_stack(deck)
    else:
        number = int(digit_pattern.search(instruction).group())
        if "deal" in instruction:
            return deal_with_increment(deck, number)
        elif "cut" in instruction:
            return cut(deck, number)
        else:
            print(f"Unknown instruction: {instruction}")
            return deck


# example 1 --------------------

deck = list(range(10))

example_instructions = """deal with increment 7
deal into new stack
deal into new stack"""

for instruction in example_instructions.splitlines():
    deck = execute_instruction(deck, instruction)
print(" ".join(map(str, deck)) == "0 3 6 9 2 5 8 1 4 7")

# example 2 --------------------

deck = list(range(10))

example_instructions = """cut 6
deal with increment 7
deal into new stack"""
expected = "3 0 7 4 1 8 5 2 9 6"

for instruction in example_instructions.splitlines():
    deck = execute_instruction(deck, instruction)

print(" ".join(map(str, deck)) == expected)

# example 3 --------------------

deck = list(range(10))

example_instructions = """deal with increment 7
deal with increment 9
cut -2"""
expected = "6 3 0 7 4 1 8 5 2 9"

for instruction in example_instructions.splitlines():
    deck = execute_instruction(deck, instruction)

print(" ".join(map(str, deck)) == expected)

# example 4 --------------------

deck = list(range(10))

example_instructions = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""
expected = "9 2 5 8 1 4 7 0 3 6"

for instruction in example_instructions.splitlines():
    deck = execute_instruction(deck, instruction)

print(" ".join(map(str, deck)) == expected)

# part 1 -----------------------------
deck = list(range(10007))
print(deck[2019])
for instruction in raw_input.splitlines():
    deck = execute_instruction(deck, instruction)

# print(f"PART ONE : {deck[2019]}")
# ↑↑↑ WRONG! They asked the position of card 2019

print(f"PART ONE : {deck.index(2019)}")

# part 2 ----------------------------------------

print("-------")


def get_previous_index_of_card(index, deck_length, instruction):
    if "deal into" in instruction:
        return deck_length - index - 1  # check
    else:
        number = int(digit_pattern.search(instruction).group())
        if "deal" in instruction:
            # i don't know why it works
            # https://twitter.com/tut_tuuut/status/1335683048264884230
            return (
                1 + index // number + number * (number - index % number)
            ) % deck_length
        elif "cut" in instruction:
            return (index + number) % deck_length
        else:
            print(f"Unknown instruction: {instruction}")
            return deck


# result 0 3 6 9 2 5 8 1 4 7
index = 9
for instr in reversed(
    """deal with increment 7
deal into new stack
deal into new stack""".splitlines()
):
    index = get_previous_index_of_card(index, 10, instr)
print("should be 7:", index)
print("------")


# result 3 0 7 4 1 8 5 2 9 6
index = 8
for instr in reversed(
    """cut 6
deal with increment 7
deal into new stack""".splitlines()
):
    index = get_previous_index_of_card(index, 10, instr)
print("should be 9:", index)
print("------")

# result 6 3 0 7 4 1 8 5 2 9
index = 0
for instr in reversed(
    """deal with increment 7
deal with increment 9
cut -2""".splitlines()
):
    print(index)
    index = get_previous_index_of_card(index, 10, instr)
print("should be 6:", index)
print("------")


index = 2020
deck_length = 119315717514047
instructions = list(raw_input.splitlines())
instructions.reverse()
for instruction in instructions:
    index = get_previous_index_of_card(index, deck_length, instruction)
    if index == 2020:
        print("aha!")
print(index)