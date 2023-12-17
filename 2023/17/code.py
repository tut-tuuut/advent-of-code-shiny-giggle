import utils as u
from collections import deque, namedtuple

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

ex = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

N, S, E, W = "N", "S", "E", "W"
DIRECTIONS = (N, S, E, W)
Step = namedtuple("Step", ["row", "col", "heat", "direction"])


def path_heat(path):
    return sum(step.heat for step in path)


def opposite(direction):
    if direction == N:
        return S
    if direction == S:
        return N
    if direction == W:
        return E
    if direction == E:
        return W


def part_1(raw_input):
    grid = tuple(
        tuple(int(char) for char in row) for row in raw_input.strip().split("\n")
    )
    HEIGHT = len(grid)
    MAX = HEIGHT - 1
    if len(grid[0]) != HEIGHT:
        raise Exception("BOUH")
    # compute an arbitrary heat sum before looking for an optimum path
    smallest_value = grid[MAX][MAX] + sum(
        grid[i][i] + grid[i][i + 1] for i in range(MAX)
    )
    initial_path = (Step(0, 0, 0, None),)  # row, column, heat, direction
    tested_paths = deque()
    tested_paths.append(initial_path)
    while len(tested_paths) > 0:
        tested_path = tested_paths.popleft()
        print(tested_path)
        if path_heat(tested_path) > smallest_value:
            continue
        last_step = tested_path[-1]
        forbidden_directions = [
            opposite(tested_path[-1].direction),
        ]
        if len(tested_path) >= 3:
            if (
                last_step.direction
                == tested_path[-2].direction
                == tested_path[-3].direction
            ):
                forbidden_directions.append(tested_path[-1].direction)


part_1(ex)
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
