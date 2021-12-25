import networkx as nx
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def debug_grid_and_path(grid, path=()):
    print(f'┌{"─"*len(grid[0])}┐')
    for y, row in enumerate(grid):
        print(f"│{u.PURPLE}", end="")
        for x, char in enumerate(row):
            if (y, x) in path:
                print(f"{u.YELLOW}{str(char)}{u.PURPLE}", end="")
            else:
                print(str(char), end="")
        print(f"{u.NORMAL}│")
    print(f'└{"─"*len(grid[0])}┘')


def get_neighbours(point, grid):
    row, col = point
    if row > 0:
        yield (row - 1, col)
    if row < len(grid) - 1:
        yield (row + 1, col)
    if col > 0:
        yield (row, col - 1)
    if col < len(grid[0]) - 1:
        yield (row, col + 1)


def find_lowest_risk_path(grid, debug=True):
    graph = nx.DiGraph()
    for row, risks in enumerate(grid):
        for col, risk in enumerate(risks):
            point = (row, col)
            for neighbour in get_neighbours(point, grid):
                graph.add_edge(neighbour, point, weight=risk)
    bottom_right = (len(grid) - 1, len(grid[0]) - 1)
    if debug:
        debug_grid_and_path(
            grid, nx.shortest_path(graph, (0, 0), bottom_right, weight="weight")
        )
    return nx.shortest_path_length(graph, (0, 0), bottom_right, weight="weight")


def part_1(raw_input):
    grid = [[int(char) for char in row] for row in raw_input.splitlines()]
    return find_lowest_risk_path(grid)


u.assert_equals(part_1(example), 40)

# u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def wrap(risk_level):
    while risk_level > 9:
        risk_level -= 9
    return risk_level


def part_2(raw_input, debug=True):
    grid = [[int(char) for char in row] for row in raw_input.splitlines()]
    new_grid = [[] for _ in range(len(grid))]
    for addenum in range(5):
        for row, risks in enumerate(grid):
            new_grid[row].extend(wrap(risk + addenum) for risk in risks)
    for addenum in range(1, 5):
        for risks in new_grid[: len(grid)]:
            new_grid.append([wrap(risk + addenum) for risk in risks])
    return find_lowest_risk_path(new_grid, debug)


u.assert_equals(part_2(example), 315)

u.answer_part_2(part_2(raw_input, debug=False))
