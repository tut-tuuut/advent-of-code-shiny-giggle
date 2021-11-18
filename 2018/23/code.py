import re
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

with open(__file__ + ".input-test.txt", "r+") as file:
    raw_test_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
def part_1(raw_input):
    row_regex = re.compile(r"pos=<(?P<x>-?\d+),(?P<y>-?\d+),(?P<z>-?\d+)>, r=(?P<r>\d+)")

    bots = [
        {
            "x": int(result["x"]),
            "y": int(result["y"]),
            "z": int(result["z"]),
            "r": int(result["r"]),
        }
        for result in (row_regex.match(row) for row in raw_input.splitlines())
    ]

    master_bot = max(bots, key=lambda bot: bot["r"])

    max_radius = master_bot["r"]

    return sum(
        1
        if max_radius
        >= abs(bot["x"] - master_bot["x"])
        + abs(bot["y"] - master_bot["y"])
        + abs(bot["z"] - master_bot["z"])
        else 0
        for bot in bots
    )

u.assert_equals(part_1(raw_test_input), 7)

u.answer_part_1(part_1(raw_input)) #652

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
