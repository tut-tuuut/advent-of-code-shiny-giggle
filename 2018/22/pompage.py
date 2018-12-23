import networkx as nx

rocky, wet, narrow = 0, 1, 2
torch, gear, neither = 0, 1, 2
valid_items = {rocky: (torch, gear), wet: (gear, neither), neither: (torch, neither)}
valid_regions = {torch: (rocky, narrow), gear: (rocky, wet), neither: (wet, narrow)}


def get_cave(file):
    with open(file) as f:
        lines = iter([line.strip() for line in f.read().strip().splitlines()])
        depth = int(next(lines)[len("depth: "):])
        target = tuple([int(n) for n in next(lines)[len("target: "):].split(",")])
    return depth, target


def generate_grid(depth, corner):
    # (x, y) -> geologic index, erosion level, risk
    grid = {}

    for y in range(0, corner[1] + 1):
        for x in range(0, corner[0] + 1):
            if (x, y) in [(0, 0), target]:
                geo = 0
            elif x == 0:
                geo = y * 48271
            elif y == 0:
                geo = x * 16807
            else:
                geo = grid[(x-1, y)][1] * grid[(x, y-1)][1]
            ero = (geo + depth) % 20183
            risk = ero % 3
            grid[(x, y)] = (geo, ero, risk)

    return grid


def dijkstra(grid, corner, target):
    graph = nx.Graph()
    for y in range(0, corner[1] + 1):
        for x in range(0, corner[0] + 1):
            items = valid_items[grid[(x, y)]]
            graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x <= corner[0] and 0 <= new_y <= corner[1]:
                    new_items = valid_items[grid[(new_x, new_y)]]
                    for item in set(items).intersection(set(new_items)):
                        graph.add_edge((x, y, item), (new_x, new_y, item), weight=1)

    return nx.dijkstra_path_length(graph, (0, 0, torch), (target[0], target[1], torch))


depth, target = get_cave("./input.txt")
grid = generate_grid(depth, target)
print("Answer 1:", sum([v[2] for v in grid.values()]))

corner = (target[0] + 100, target[1] + 100)
grid = {c: v[2] for c, v in (generate_grid(depth, corner)).items()}
print("Answer 2:", dijkstra(grid, corner, target))