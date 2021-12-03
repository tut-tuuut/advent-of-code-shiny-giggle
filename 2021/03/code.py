import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

raw_example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_power_consumption(raw_input):
    rows = raw_input.splitlines()
    first_row = rows[0]
    width = len(first_row)
    length = len(rows)
    gamma_string = "".join(
        "0" if [r[bit] for r in rows].count("0") > length / 2 else "1"
        for bit in range(width)
    )
    epsilon_string = "".join("0" if c == "1" else "1" for c in gamma_string)
    return int(gamma_string, 2) * int(epsilon_string, 2)


u.assert_equals(get_power_consumption(raw_example), 198)
u.answer_part_1(get_power_consumption(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_life_support_rating(raw_input):
    rows = raw_input.splitlines()
    first_row = rows[0]
    width = len(first_row)
    length = len(rows)
    oxygen = rows.copy()
    co2 = rows.copy()
    for bit in range(width):
        o2_sum = sum(int(r[bit]) for r in oxygen)
        o2_criteria = str(int(o2_sum >= len(oxygen) / 2))
        oxygen = [r for r in oxygen if r[bit] == o2_criteria]
        if len(oxygen) == 1:
            break
    for bit in range(width):
        co2_sum = sum(int(r[bit]) for r in co2)
        co2_criteria = str(int(co2_sum < len(co2) / 2))
        co2 = [r for r in co2 if r[bit] == co2_criteria]
        if len(co2) == 1:
            break
    return int(oxygen[0], 2) * int(co2[0], 2)


u.assert_equals(get_life_support_rating(raw_example), 230)
u.answer_part_2(get_life_support_rating(raw_input))
