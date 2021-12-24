from networkx.algorithms.shortest_paths.generic import shortest_path_length
import utils as u
import networkx as nx

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()


# ┌───┬───┬───┬───┬────┬───┬────┬───┬────┬───┬───┐
# │ 0 │ 1 │   │ 2 │    │ 3 │    │ 4 │    │ 5 │ 6 │
# └───┴───┼───┼───┼────┼───┼────┼───┼────┼───┴───┘
#         │ 7 │   │ 9  │   │ 11 │   │ 13 │
#         ├───┤   ├────┤   ├────┤   ├────┤
#         │ 8 │   │ 10 │   │ 12 │   │ 14 │
#         └───┘   └────┘   └────┘   └────┘

distances = nx.Graph()
distances.add_edges_from(
    [
        (0, 1, {"weight": 1}),
        (1, 2, {"weight": 2}),
        (1, 7, {"weight": 2}),
        (7, 2, {"weight": 2}),
        (7, 8, {"weight": 1}),
        (2, 9, {"weight": 2}),
        (2, 3, {"weight": 2}),
        (9, 3, {"weight": 2}),
        (9, 10, {"weight": 1}),
        (3, 11, {"weight": 2}),
        (3, 4, {"weight": 2}),
        (11, 4, {"weight": 2}),
        (11, 12, {"weight": 1}),
        (4, 5, {"weight": 2}),
        (4, 13, {"weight": 2}),
        (13, 5, {"weight": 2}),
        (13, 14, {"weight": 1}),
        (5, 6, {"weight": 1}),
    ]
)

u.assert_equals(nx.shortest_path_length(distances, 8, 6, weight="weight"), 10)
u.assert_equals(nx.shortest_path_length(distances, 14, 0, weight="weight"), 10)


COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

HALLWAY = tuple(range(7))
ROOMS = tuple(range(7, 15))

TARGET = (
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "A",
    "A",
    "B",
    "B",
    "C",
    "C",
    "D",
    "D",
)

ROOMS_BY_LETTER = {
    "A": (7, 8),
    "B": (9, 10),
    "C": (11, 12),
    "D": (13, 14),
}

example_state = (
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "B",
    "A",
    "C",
    "D",
    "B",
    "C",
    "D",
    "A",
)
u.assert_equals(len(example_state), 15)
u.assert_equals(example_state[7], "B")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_1(initial_state):
    state_graphs = nx.DiGraph()
    state_graphs.add_node(initial_state)


u.assert_equals(part_1(example_state), 12521)

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
