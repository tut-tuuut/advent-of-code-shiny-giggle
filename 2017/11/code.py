import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

examples = {
    "ne,ne,ne": 3,
    "ne,ne,sw,sw": 0,
    "ne,ne,s,s": 2,
    "se,sw,se,sw,sw": 3,
}

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# Axes : (cf. https://www.redblobgames.com/grids/hexagons/#coordinates-cube)
#   +s  -r
#     \ /
# -q --+-- +q
#     / \
#   +r   -s
#
def get_distance_from_path(path):
    q, r, s = 0, 0, 0
    for step in path.split(","):
        if step == "n":
            s += 1
            r -= 1
        elif step == "s":
            r += 1
            s -= 1
        elif step == "ne":
            r -= 1
            q += 1
        elif step == "se":
            q += 1
            s -= 1
        elif step == "sw":
            q -= 1
            r += 1
        elif step == "nw":
            q -= 1
            s += 1
    return int((abs(q) + abs(r) + abs(s)) / 2)


for path, distance in examples.items():
    u.assert_equals(get_distance_from_path(path), distance)

u.answer_part_1(get_distance_from_path(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_further_during_path(path):
    q, r, s = 0, 0, 0
    further = 0
    for step in path.split(","):
        if step == "n":
            s += 1
            r -= 1
        elif step == "s":
            r += 1
            s -= 1
        elif step == "ne":
            r -= 1
            q += 1
        elif step == "se":
            q += 1
            s -= 1
        elif step == "sw":
            q -= 1
            r += 1
        elif step == "nw":
            q -= 1
            s += 1
        current_position = int((abs(q) + abs(r) + abs(s)) / 2)
        if current_position > further:
            further = current_position
    return further


u.answer_part_2(get_further_during_path(raw_input))
