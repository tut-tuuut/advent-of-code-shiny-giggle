import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_coordinates(raw_input):
    numbers_coordinates = {}
    symbols_coordinates = {}
    for row, row_contents in enumerate(raw_input.split()):
        current_number_digits = []
        for col, char in enumerate(row_contents):
            if char.isdigit():
                current_number_digits.append(char)
            elif len(current_number_digits) > 0:
                # we found a number, let's store the coordinates of its last digit
                numbers_coordinates[(row, col - 1)] = "".join(
                    current_number_digits
                )  # store as string bc I will use its length
                current_number_digits = []
            if not char.isdigit() and char != ".":
                # we found a symbol, let's store its coordinates
                symbols_coordinates[(row, col)] = char
        # deal with numbers at the end of a row:
        if len(current_number_digits):
            numbers_coordinates[(row, len(row_contents) - 1)] = "".join(
                current_number_digits
            )
    return numbers_coordinates, symbols_coordinates


def part_1(raw_input):
    # Find numbers and symbols in grid -----------------------
    numbers_coordinates, symbols_coordinates = extract_coordinates(raw_input)

    # print(numbers_coordinates)
    # print(symbols_coordinates)

    # Find numbers which are adjacent to a symbol
    result_sum = 0
    for coords, value in numbers_coordinates.items():
        number_row, number_col = coords
        found = False
        # u.pink(f"{coords} : {value}")
        for row in range(number_row - 1, number_row + 2):
            if found:
                break
            for col in range(number_col - len(value), number_col + 2):
                if (row, col) in symbols_coordinates:
                    result_sum += int(value)
                    found = True
                    # u.yellow(f"({row},{col}) : {symbols_coordinates[(row,col)]}")
                    break
    return result_sum


u.assert_equal(part_1(example_input), 4361)

u.answer_part_1(part_1(raw_input))


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(raw_input):
    numbers_coordinates, symbols_coordinates = extract_coordinates(raw_input)
    # for each star_symbol, we will store each adjacent number coordinate in a set
    star_symbols = {
        coords: set() for coords, symbol in symbols_coordinates.items() if symbol == "*"
    }
    # loop over numbers and check adjacency with * symbols
    for coords, value in numbers_coordinates.items():
        number_row, number_col = coords
        for row in range(number_row - 1, number_row + 2):
            for col in range(number_col - len(value), number_col + 2):
                if (row, col) in star_symbols:
                    star_symbols[(row, col)].add(coords)
    result_sum = 0
    for adjacent_set in star_symbols.values():
        if len(adjacent_set) == 2:
            product = 1
            for x in adjacent_set:
                product = product * int(numbers_coordinates[x])
            result_sum += product
    return result_sum


u.assert_equal(part_2(example_input), 467835)

u.answer_part_2(part_2(raw_input))
