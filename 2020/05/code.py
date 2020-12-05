import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_place_coordinates(boarding_pass):
    row_instructions = boarding_pass[:-3]
    col_instructions = boarding_pass[-3:]
    # hey you know what, it's a binary number where B = 1 and F = 0
    row_binary = row_instructions.replace("F", "0").replace("B", "1")
    # or where R = 1 and L = 0
    col_binary = col_instructions.replace("L", "0").replace("R", "1")
    return (int(row_binary, base=2), int(col_binary, base=2))


def get_place_id(row, col):
    return 8 * row + col


u.assert_equals(get_place_coordinates("BFFFBBFRRR"), (70, 7))
u.assert_equals(get_place_coordinates("FFFBBBFRRR"), (14, 7))
u.assert_equals(get_place_coordinates("BBFFBBFRLL"), (102, 4))


u.assert_equals(get_place_id(70, 7), 567)
u.assert_equals(get_place_id(14, 7), 119)
u.assert_equals(get_place_id(102, 4), 820)

place_ids = [
    get_place_id(*get_place_coordinates(boarding_pass))
    for boarding_pass in raw_input.splitlines()
]

u.answer_part_1(max(place_ids))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

sorted_place_ids = sorted(place_ids)

for i in range(1, len(sorted_place_ids) - 1):
    seat_id = sorted_place_ids[i]
    next_seat_id = sorted_place_ids[i + 1]
    if seat_id + 1 != next_seat_id:
        u.answer_part_2(seat_id + 1)
        break

# another method using a comprehension, but i'm not sure it's clearer
for seat_id, next_seat_id in (
    (sorted_place_ids[i : i + 2]) for i in range(len(sorted_place_ids) - 1)
):
    if seat_id + 1 != next_seat_id:
        u.answer_part_2(seat_id + 1)
        break
