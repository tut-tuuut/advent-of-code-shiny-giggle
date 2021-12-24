from networkx.algorithms.shortest_paths.generic import shortest_path_length
import utils as u
import networkx as nx

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()


# ┌───┬───┬────┬───┬────┬───┬────┬───┬────┬───┬───┐
# │ 0 │ 1 │    │ 2 │    │ 3 │    │ 4 │    │ 5 │ 6 │
# └───┴───┼────┼───┼────┼───┼────┼───┼────┼───┴───┘
#         │  7 │   │ 11 │   │ 15 │   │ 19 │
#         ├────┤   ├────┤   ├────┤   ├────┤
#         │  8 │   │ 12 │   │ 16 │   │ 20 │
#         ├────┤   ├────┤   ├────┤   ├────┤
#         │  9 │   │ 13 │   │ 17 │   │ 21 │
#         ├────┤   ├────┤   ├────┤   ├────┤
#         │ 10 │   │ 14 │   │ 18 │   │ 22 │
#         └────┘   └────┘   └────┘   └────┘
#            A        B        C        D

distances = nx.Graph()
distances_edges = (
    # left : 1-2
    (0, 1, 1),
    # cross 1-2-7
    (1, 2, 2),
    (1, 7, 2),
    (7, 2, 2),
    # branch A : 7-8-9-10
    (7, 8, 1),
    (8, 9, 1),
    (9, 10, 1),
    # cross 2-11-3
    (2, 11, 2),
    (2, 3, 2),
    (11, 3, 2),
    # branch B : 11-12-13-14
    (11, 12, 1),
    (12, 13, 1),
    (13, 14, 1),
    # cross 3-4-15
    (3, 4, 2),
    (3, 15, 2),
    (4, 15, 2),
    # branch C : 15-16-17-18
    (15, 16, 1),
    (16, 17, 1),
    (17, 18, 1),
    # cross 4-5-19
    (4, 5, 2),
    (5, 19, 2),
    (4, 19, 2),
    # branch D : 19-20-21-22
    (19, 20, 1),
    (20, 21, 1),
    (21, 22, 1),
    # right : 5-6
    (5, 6, 1),
)
for n1, n2, w in distances_edges:
    distances.add_edge(n1, n2, weight=w)

u.assert_equals(nx.shortest_path_length(distances, 8, 6, weight="weight"), 10)
u.assert_equals(nx.shortest_path_length(distances, 14, 0, weight="weight"), 8)


COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

HALLWAY = tuple(range(7))

ROOMS_BY_LETTER = {
    "A": (7, 8, 9, 10),
    "B": (11, 12, 13, 14),
    "C": (15, 16, 17, 18),
    "D": (19, 20, 21, 22),
}

TARGET = (None,) * 6 + ("A",) * 4 + ("B",) * 4 + ("C",) * 4 + ("D",) * 4


example_state = (
    (None,) * 7 + tuple("BDDA") + tuple("CCBD") + tuple("BBAC") + tuple("DACA")
)

u.assert_equals(len(example_state), 15)
u.assert_equals(example_state[7], "B")

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

def part_1(initial_state):
    state_graphs = nx.DiGraph()
    state_graphs.add_node(initial_state)


u.assert_equals(part_1(example_state), 12521)

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
