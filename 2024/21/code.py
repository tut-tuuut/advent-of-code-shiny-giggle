import utils as u
import networkx as nx
from itertools import pairwise

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+


    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

"""

NUMERIC_KEYBOARD = nx.DiGraph()
NUMERIC_KEYBOARD.add_node("A")
NUMERIC_KEYBOARD.add_nodes_from(str(x) for x in range(10))

rows = ("789", "456", "123", "0A")
for row in rows:
    for left, right in pairwise(row):
        NUMERIC_KEYBOARD.add_edge(left, right, label=">", weight=1)
        NUMERIC_KEYBOARD.add_edge(right, left, label="<", weight=1)

cols = ("741", "8520", "963A")
for col in cols:
    for t, b in pairwise(col):
        NUMERIC_KEYBOARD.add_edge(t, b, label="v", weight=1)
        NUMERIC_KEYBOARD.add_edge(b, t, label="^", weight=1)

print(nx.all_shortest_paths(NUMERIC_KEYBOARD, "A", "2"))
print(nx.shortest_path(NUMERIC_KEYBOARD, "A","2"))


def type_on_keyboard(str_to_type, keyboard):
    starting = "A"
    for cur,nex in pairwise(f"A{str_to_type}"):
        directions = []
        for x,y in pairwise(nx.shortest_path(keyboard, cur, nex)):
            directions.append(NUMERIC_KEYBOARD.get_edge_data(x, y)["label"])
        directions.append("A")
        print("".join(directions))

type_on_keyboard("029A", NUMERIC_KEYBOARD)
u.answer_part_1("allez")

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
