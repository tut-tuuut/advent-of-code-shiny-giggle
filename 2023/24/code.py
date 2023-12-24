import utils as u
from collections import namedtuple
from itertools import combinations

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

Hailstone = namedtuple("Hailstone", ["x", "y", "z", "vx", "vy", "vz"])

ex = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def det(vax, vay, vbx, vby):
    return vax * vby - vay * vbx


def y_for_given_x(x, a: Hailstone):
    return a.vy * x / a.vx + a.y - a.x * a.vy / a.vx


def x_for_given_y(y, a: Hailstone):
    return (a.vx / a.vy) * (y - a.y - a.x * a.vy / a.vx)


def part_1(raw_input, low=7, high=27, debug=True):
    stones = []
    for row in raw_input.strip().split("\n"):
        pos, vel = row.split(" @ ")
        x, y, z = (int(nb) for nb in pos.split(", "))
        vx, vy, vz = (int(nb) for nb in vel.split(", "))
        stone = Hailstone(x, y, z, vx, vy, vz)
        stones.append(stone)
    intersections = 0
    for a, b in combinations(stones, 2):
        if det(a.vx, a.vy, b.vx, b.vy) == 0:
            # a and b velocities are colinear: no intersection
            continue

        # compare ya and yb for xmin and xmax : if they don't switch order,
        # there is no intersection between xmin and xmax
        y_a_min = y_for_given_x(low, a)
        y_a_max = y_for_given_x(high, a)
        y_b_min = y_for_given_x(low, b)
        y_b_max = y_for_given_x(high, b)

        # if both differences are of the same sign,
        # a and b did not switch order on y axis between xmin and xmax:
        # it's not interesting for us
        if (y_a_max - y_b_max) * (y_a_min - y_b_min) > 0:
            continue

        # compare x for ymin and ymax: they must switch order
        x_a_min = x_for_given_y(low, a)
        x_a_max = x_for_given_y(high, a)
        x_b_min = x_for_given_y(low, b)
        x_b_max = x_for_given_y(high, b)

        if (x_a_max - x_b_max) * (x_a_min - x_b_min) > 0:
            continue
        if debug:
            print("intersection for", a, b)
        intersections += 1
    return intersections


print(part_1(ex))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
