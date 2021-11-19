import re
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

with open(__file__ + ".input-test.txt", "r+") as file:
    raw_test_input = file.read()

with open(__file__ + ".input-test-2.txt", "r+") as file:
    raw_test_input_2 = file.read()


def get_bots_from_raw_input(raw_input):
    row_regex = re.compile(
        r"pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>, r=(?P<r>\d+)"
    )
    return [
        {
            "x": int(result["x"]),
            "y": int(result["y"]),
            "z": int(result["z"]),
            "r": int(result["r"]),
        }
        for result in (row_regex.match(row) for row in raw_input.splitlines())
    ]


def bot_distance(a, b):
    return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"]) + abs(a["z"] - b["z"])


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
def part_1(raw_input):
    bots = get_bots_from_raw_input(raw_input)

    master_bot = max(bots, key=lambda bot: bot["r"])

    max_radius = master_bot["r"]

    return sum(1 if max_radius >= bot_distance(bot, master_bot) else 0 for bot in bots)


u.assert_equals(part_1(raw_test_input), 7)

u.answer_part_1(part_1(raw_input))  # 652

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def distance(x, y, z, bot):
    return abs(x - bot["x"]) + abs(y - bot["y"]) + abs(z - bot["z"])


def how_many_in_range(x, y, z, bots):
    return sum(1 if bot["r"] >= distance(x, y, z, bot) else 0 for bot in bots)


bots = get_bots_from_raw_input(raw_test_input_2)

# find the points which are in range of the most nanobots
nb_bots = len(bots)

# answer = shortest manhattan distance between one of those points and (0,0,0)

# answer for test = (12,12,12) is in range of 5 nanobots => answer = 36
u.assert_equals(how_many_in_range(12, 12, 12, bots), 5)
