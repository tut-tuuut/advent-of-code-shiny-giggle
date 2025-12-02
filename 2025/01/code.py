import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_1(s_input):
    position = 50
    password = 0
    for row in s_input.splitlines():
        direction = -1 if row[0] == "L" else 1
        amount = int(row[1:])
        position = (position + direction * amount) % 100
        if position == 0:
            password = password + 1
    return password


example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

u.assert_equal(part_1(example_input), 3)

u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(s_input):
    position = 50
    password = 0
    for row in s_input.splitlines():
        # print("--------")
        # print(row)
        direction = -1 if row[0] == "L" else 1
        amount = int(row[1:])
        move = direction * amount
        final_position = position + move
        # print("final position",final_position)
        if not (0 <= final_position < 100):
            begin = position if direction == -1 else 100 - position
            rab = final_position % 100 if direction == 1 else 100 - final_position % 100
            turns = (abs(move) - begin - rab) // 100
            # print(f"{begin=}")
            # print(f"{rab=}")
            # print(f"{turns=}")

            password = password + 1 + turns
            if rab == 0 or begin == 0:
                password = password - 1
                # print(f"password - 1")
            # print(f"password + {turns + 1}")
        position = final_position % 100
        # print(f"{position=}")
        if position == 0:
            password = password + 1
            # print("password + 1")

    return password


u.assert_equal(part_2(example_input), 6)
u.assert_equal(part_2("R1000"), 10)

u.answer_part_2(part_2(raw_input))

# 7239 too high
