import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_input_row(input_row):
    semicolon = input_row.index(":")
    pipe = input_row.index("|")
    winner_numbers = set(int(x) for x in input_row[semicolon + 1 : pipe].split())
    owned_numbers = set(int(x) for x in input_row[pipe + 1 :].split())
    return winner_numbers, owned_numbers


def part_1(raw_input):
    result_sum = 0
    for row in raw_input.strip().split("\n"):
        winner_numbers, owned_numbers = parse_input_row(row)
        owned_winner_numbers = winner_numbers & owned_numbers
        if len(owned_winner_numbers):
            result_sum += pow(2, len(owned_winner_numbers) - 1)
    return result_sum


u.assert_equal(part_1(example_input), 13)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(raw_input):
    clean_input = raw_input.strip().split("\n")
    card_counts = {card_id: 1 for card_id in range(1, len(clean_input) + 1)}
    for x, row in enumerate(raw_input.strip().split("\n")):
        current_card_id = x + 1
        current_card_count = card_counts[current_card_id]
        winner_numbers, owned_numbers = parse_input_row(row)
        owned_winner_numbers = winner_numbers & owned_numbers
        if len(owned_winner_numbers):
            for copy_id in range(
                current_card_id + 1, current_card_id + len(owned_winner_numbers) + 1
            ):
                card_counts[copy_id] = current_card_count + card_counts[copy_id]
    return sum(card_counts.values())


u.assert_equal(part_2(example_input), 30)

u.answer_part_2(part_2(raw_input))
