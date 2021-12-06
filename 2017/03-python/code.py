import utils as u
from itertools import product
from collections import defaultdict
from itertools import count

input = 289326

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


def next_position(current_direction, x, y):
    next_direction = current_direction
    if current_direction == EAST:
        if x == -y + 1:
            next_direction = NORTH
    elif current_direction == WEST:
        if x == -y:
            next_direction = SOUTH
    elif x == y:
        if x > 0:
            next_direction = WEST
        elif x < 0:
            next_direction = EAST
    dx, dy = next_direction
    return next_direction, x + dx, y + dy


def part_2(target):
    x = 0
    y = 0
    values = defaultdict(lambda: 0)
    values[0, 0] = 1
    direction = EAST
    for _ in count(1):
        direction, x, y = next_position(direction, x, y)
        current_value = sum(
            values[x, y] for x, y in product(range(x - 1, x + 2), range(y - 1, y + 2))
        )
        values[x, y] = current_value
        if current_value > target:
            return current_value


u.answer_part_2(part_2(input))
