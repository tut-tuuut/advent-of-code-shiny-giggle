from math import prod
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_1(raw_input):
    result_sum = 0
    for i, row in enumerate(raw_input.strip().split("\n")):
        game_id = i + 1
        _, raw_sets = row.split(": ")
        is_game_possible = True
        for raw_set in raw_sets.split("; "):
            if is_game_possible:
                for digit_color in raw_set.split(", "):
                    digit, color = digit_color.split()
                    digit = int(digit)
                    # only 12 red cubes, 13 green cubes, and 14 blue cubes
                    if digit > 12 and color == "red":
                        is_game_possible = False
                    elif digit > 13 and color == "green":
                        is_game_possible = False
                    elif digit > 14 and color == "blue":
                        is_game_possible = False
        if is_game_possible:
            result_sum += game_id
    return result_sum


u.assert_equal(part_1(example_input), 8)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(raw_input):
    result_sum = 0
    for row in raw_input.strip().split("\n"):
        _, raw_sets = row.split(": ")
        min_counts = {"red": 0, "blue": 0, "green": 0}
        for raw_set in raw_sets.split("; "):
            for digit_color in raw_set.split(", "):
                digit, color = digit_color.split()
                digit = int(digit)
                # only 12 red cubes, 13 green cubes, and 14 blue cubes
                if digit > min_counts.get(color):
                    min_counts[color] = digit
        result_sum += prod(min_counts.values())
    return result_sum


u.assert_equal(part_2(example_input), 2286)

u.answer_part_2(part_2(raw_input))
