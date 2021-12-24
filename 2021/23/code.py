from networkx.algorithms.shortest_paths import weighted
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

REACHABLE_FROM_ROOM = {
    "A": ((1, 0), (2, 3, 4, 5, 6)),
    "B": ((2, 1, 0), (3, 4, 5, 6)),
    "C": ((3, 2, 1, 0), (4, 5, 6)),
    "D": ((4, 3, 2, 1, 0), (5, 6)),
}

TARGET = (None,) * 7 + ("A",) * 4 + ("B",) * 4 + ("C",) * 4 + ("D",) * 4


example_state = (
    (None,) * 7 + tuple("BDDA") + tuple("CCBD") + tuple("BBAC") + tuple("DACA")
)

u.assert_equals(len(example_state), 15)
u.assert_equals(example_state[7], "B")


def debug_state(state):
    def s(char):
        if char is None:
            return "."
        else:
            return char

    print("┌───────────┐")
    print(
        f"│{s(state[0])}{s(state[1])} {s(state[2])} {s(state[3])} {s(state[4])} {s(state[5])}{s(state[6])}│"
    )
    print("└─┐       ┌─┘")
    print(f"  │{s(state[7])}│{s(state[11])}│{s(state[15])}│{s(state[19])}│")
    print(f"  │{s(state[8])}│{s(state[12])}│{s(state[16])}│{s(state[20])}│")
    print(f"  │{s(state[9])}│{s(state[13])}│{s(state[17])}│{s(state[21])}│")
    print(f"  │{s(state[10])}│{s(state[14])}│{s(state[18])}│{s(state[22])}│")
    print("  └─┴─┴─┴─┘")


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_1(initial_state):
    state_graphs = nx.DiGraph()
    state_graphs.add_node(initial_state)
    to_explore = set()
    to_explore.add(initial_state)
    explored = set()
    while len(to_explore):
        current_state = to_explore.pop()
        if current_state in explored:
            continue
        explored.add(current_state)
        # debug_state(current_state)
        # print(current_state)
        # print('────────────────────────────────────────────')
        # can we pop some letters out of the branchs into the hallways?
        for room in ("A", "B", "C", "D"):
            for i, position in enumerate(ROOMS_BY_LETTER[room]):
                if current_state[position] == None:
                    continue
                letter = current_state[position]
                if letter == room and all(
                    room == current_state[pos] for pos in ROOMS_BY_LETTER[room][i:]
                ):
                    # branch is filled, do not move these letters
                    break
                for reachable_hallways in REACHABLE_FROM_ROOM[room]:
                    for target in reachable_hallways:
                        if current_state[target] != None:
                            break
                        reachable_target = True
                        for intermediate in nx.shortest_path(
                            distances, position, target
                        ):
                            if (
                                current_state[intermediate] != None
                                and intermediate != position
                            ):
                                print(f"intermediate {intermediate} is occupied")
                                reachable_target = False
                                break
                        if not reachable_target:
                            continue
                        new_state = list(current_state)
                        new_state[target] = letter
                        new_state[position] = None
                        new_state = tuple(new_state)
                        state_graphs.add_edge(
                            current_state,
                            new_state,
                            weight=COSTS[letter]
                            * nx.shortest_path_length(
                                distances, target, position, weight="weight"
                            ),
                        )
                        to_explore.add(new_state)
                break  # once we moved a letter in the room, no other letter moves
        # can we put some letters from the hallway into the correct room?
        for position in HALLWAY:
            letter = current_state[position]
            if letter == None:
                continue
            if all(pos in (None, letter) for pos in ROOMS_BY_LETTER[letter]):
                target = max(
                    pos for pos in ROOMS_BY_LETTER[letter] if current_state[pos] == None
                )
                # check target is reachable from position, using distances
                reachable_target = True
                for intermediate in nx.shortest_path(distances, position, target):
                    if current_state[intermediate] != None and intermediate != position:
                        reachable_target = False
                if not reachable_target:
                    continue  # check another hallway position
                new_state = list(current_state)
                new_state[position] = None
                new_state[target] = letter
                new_state = tuple(new_state)
                state_graphs.add_edge(
                    current_state,
                    new_state,
                    weight=nx.shortest_path_length(distances, position, target)
                    * COSTS[letter],
                )
    for intermediary_state in nx.shortest_path(
        state_graphs,
        initial_state,
        (
            None,
            "B",
            "A",
            "A",
            "B",
            "C",
            "D",
            "B",
            "D",
            "D",
            "A",
            "C",
            "C",
            "B",
            "D",
            None,
            None,
            None,
            "C",
            None,
            None,
            None,
            "A",
        ),
    ):
        debug_state(intermediary_state)
    # return nx.shortest_path_length(state_graphs, initial_state, TARGET, weight="weight")


u.assert_equals(part_1(example_state), 12521)

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
