from math import prod

import networkx as nx

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()
with open(__file__ + ".example.txt", "r+") as file:
    example_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_tile_borders(raw_tileset: str):
    tileset = {}
    for raw_tile_description in raw_tileset.split("\n\n"):
        tile_data = raw_tile_description.splitlines()
        tile_title = tile_data.pop(0)
        tile_number = int(tile_title[5:9])  # all tiles have 4-digits numbers
        tileset[tile_number] = (
            tile_data[0],  # top
            "".join(tile_row[-1] for tile_row in tile_data),  # right
            tile_data[-1],  # bottom
            "".join(tile_row[0] for tile_row in tile_data),  # left
        )
    return tileset


def build_contact_graph(raw_tileset):
    borders = parse_tile_borders(raw_tileset)
    contacts = nx.Graph()
    for tile_id, tile_borders in borders.items():
        for other_tile_id, other_borders in borders.items():
            if tile_id == other_tile_id:
                continue
            for border in tile_borders:
                if border in other_borders:
                    contacts.add_edge(tile_id, other_tile_id)
                if border[::-1] in other_borders:
                    contacts.add_edge(tile_id, other_tile_id)
    return contacts


def find_corner_tiles(raw_tileset):
    contacts = build_contact_graph(raw_tileset)
    # in contacts graph:
    # - insider tiles have 4 neighbors
    # - border tiles have 3 neighbors
    # - corner tiles have 2 neighbors
    return [
        node
        for node in contacts.nodes()
        if len(list(nx.neighbors(contacts, node))) == 2
    ]


u.assert_equals(prod(find_corner_tiles(example_input)), 20899048083289)
u.answer_part_1(prod(find_corner_tiles(raw_input)))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

DIRECTIONS = ("Top", "Right", "Bottom", "Left")


class Tile:
    def __init__(self, raw_description):
        tile_data = raw_description.splitlines()
        tile_title = tile_data.pop(0)
        self.id = int(tile_title[5:9])  # all tiles have 4-digits numbers
        self.borders = [
            tile_data[0],  # top
            "".join(tile_row[-1] for tile_row in tile_data),  # right
            tile_data[-1],  # bottom
            "".join(tile_row[0] for tile_row in tile_data),  # left
        ]
        for border in self.borders:
            if border == border[::-1]:
                print(f"{self.id} will be a problem")
        # self.inner = [row[1:-1] for row in tile_data[1:-1]]
        self.inner = tile_data
        self.size = len(self.inner[0])
        self.neighbors = {}
        self.locked = False

    def __str__(self):
        return "\n".join(self.inner)

    def rotate_clockwise(self, times: int):
        print(f"rotate {self.id} {times} times")
        if times % 4 == 0:
            return
        self.borders = [self.borders[(i - times) % 4] for i in range(4)]
        if times == 1 or times == 3:
            self.inner = [
                "".join(row[i] for row in self.inner[::-1]) for i in range(self.size)
            ]
        if times == 2 or times == 3:
            self.inner = [row[::-1] for row in self.inner[::-1]]

    def flip(self, axis: int):
        print(f"flip {self.id} on axis {DIRECTIONS[axis]}")
        if axis == TOP or axis == BOTTOM:
            # vertical axis: flip every row individually
            self.inner = [row[::-1] for row in self.inner]
            # flip top and bottom borders
            self.borders[TOP] = self.borders[TOP][::-1]
            self.borders[BOTTOM] = self.borders[BOTTOM][::-1]
        if axis == LEFT or axis == RIGHT:
            # horizontal axis: flip row order without flipping them individually
            self.inner = self.inner[::-1]
            # flip left and right borders
            self.borders[LEFT] = self.borders[LEFT][::-1]
            self.borders[RIGHT] = self.borders[RIGHT][::-1]

    def addNeighbor(self, direction: int, neighbor):
        if direction not in self.neighbors:
            self.neighbors[direction] = neighbor
            print(f"placing {neighbor.id} at {DIRECTIONS[direction]} of {self.id}.")
        elif self.neighbors[direction] != neighbor:
            raise RuntimeError(
                f"two tiles at the same place! {neighbor.id} and {self.neighbors[direction].id}"
            )


def build_tile_objects_dict(raw_tileset: str):
    tileset = {}
    for raw_tile in raw_tileset.split("\n\n"):
        tile = Tile(raw_tile)
        tileset[tile.id] = tile
    return tileset


def analyze_graph(graph: nx.Graph):
    """check the graph we have built is well-formed:
    ideally you have 4 corners, not less,
    edges count is a multiple of 4,
    and insiders count is the square of edges_count/4.
    (If not, good luck to you, I cannot help.)
    """
    print(f"{len(graph)} tiles total")
    counts = {i: 0 for i in range(2, 5)}
    for n in graph.nodes():
        neighbors_count = len(list(nx.neighbors(graph, n)))
        counts[neighbors_count] += 1
    corners = counts[2]
    edges = counts[3]
    insiders = counts[4]
    print(f"-> {corners} corners")
    print(f"-> {edges} edges")
    print(f"-> {insiders} insiders")
    if corners != 4 or edges % 4 > 0 or (edges / 4) ** 2 != insiders:
        print(f"{u.RED}Your graph is pourri!{u.NORMAL}")
    else:
        print(f"{u.GREEN}Your graph is OK!{u.NORMAL}")


def tuple_intersection(t: tuple, u: tuple):
    for tx in t:
        if tx in u:
            return tx


def place_neighbor_of_locked_tile(locked: Tile, neighbor: Tile):
    if not locked.locked:
        print("uh that smells!")
    print("---")
    print(f"placing tile {neighbor.id} next to {locked.id}")
    print(f"tile {neighbor.id}:")
    print(neighbor)
    print(f"tile {locked.id} (locked):")
    print(locked)
    common_border = tuple_intersection(locked.borders, neighbor.borders)
    if common_border:
        direction_for_locked = locked.borders.index(common_border)
        direction_for_neighbor = neighbor.borders.index(common_border)
        print(f"direction for {locked.id}: {DIRECTIONS[direction_for_locked]}")
        print(f"direction for {neighbor.id}: {DIRECTIONS[direction_for_neighbor]}")
        if (direction_for_locked - direction_for_neighbor) % 4 == 2:
            print("diff == 2")
            locked.addNeighbor(direction_for_locked, neighbor)
            neighbor.addNeighbor(direction_for_neighbor, locked)
            neighbor.locked = True
        elif direction_for_locked == direction_for_neighbor:
            print("diff == 0")
            neighbor.flip((direction_for_locked + 1) % 4)
            locked.addNeighbor(direction_for_locked, neighbor)
            neighbor.addNeighbor((direction_for_locked + 2) % 4, locked)
            neighbor.locked = True
        elif direction_for_locked == (direction_for_neighbor + 1) % 4:
            print("diff == 1")
            neighbor.rotate_clockwise(3)
            locked.addNeighbor(direction_for_locked, neighbor)
            neighbor.addNeighbor((direction_for_locked + 2) % 4, locked)
            neighbor.locked = True
        elif direction_for_locked == (direction_for_neighbor - 1) % 4:
            print("diff == -1")
            neighbor.rotate_clockwise(1)
            locked.addNeighbor(direction_for_locked, neighbor)
            neighbor.addNeighbor((direction_for_locked + 2) % 4, locked)
            neighbor.locked = True
    else:
        common_border = tuple_intersection(
            locked.borders, tuple(border[::-1] for border in neighbor.borders)
        )
        direction_for_locked = locked.borders.index(common_border)
        direction_for_neighbor = neighbor.borders.index(common_border[::-1])
        print(f"direction for {locked.id}: {DIRECTIONS[direction_for_locked]}")
        print(f"direction for {neighbor.id}: {DIRECTIONS[direction_for_neighbor]}")
        if direction_for_locked == direction_for_neighbor:
            print("fdiff == 0")
            neighbor.rotate_clockwise(2)
            locked.addNeighbor(direction_for_locked, neighbor)
            neighbor.addNeighbor((direction_for_locked + 2) % 4, locked)
            neighbor.locked = True
        elif (direction_for_locked - direction_for_neighbor) % 4 == 2:
            print("fdiff == 2")
            neighbor.flip((direction_for_locked) % 4)
            locked.addNeighbor(direction_for_locked, neighbor)
            neighbor.addNeighbor((direction_for_locked + 2) % 4, locked)
            neighbor.locked = True
        elif direction_for_locked == (direction_for_neighbor + 1) % 4:
            print("fdiff == 1")
            print("todo 4")
        elif direction_for_locked == (direction_for_neighbor - 1) % 4:
            print("fdiff == -1")
            print("todo 5")


def assemble_jigsaw(tiles: dict, contacts: nx.Graph):
    any_tile_id = next(iter(tiles))
    todo_list = [tiles[any_tile_id]]
    while len(todo_list) > 0:
        todo = todo_list.pop(0)
        todo.locked = True
        if len(todo.neighbors) == 4:
            continue
        for neighbor_id in nx.neighbors(contacts, todo.id):
            neighbor = tiles[neighbor_id]
            place_neighbor_of_locked_tile(todo, neighbor)
            todo_list.append(neighbor)
        if 0 == sum(1 for tile in tiles.values() if not tile.locked):
            break


examples = build_tile_objects_dict(example_input)
example_graph = build_contact_graph(example_input)
analyze_graph(example_graph)
assemble_jigsaw(examples, example_graph)

first_corner_id = find_corner_tiles(example_input)[0]
first_corner = examples[first_corner_id]

# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
top_left_corner = [
    tile
    for tile in examples.values()
    if TOP not in tile.neighbors and LEFT not in tile.neighbors
][0]

print(f"top left corner : {top_left_corner.id}")
while True:
    display = top_left_corner
    while True:
        print(display.id, end=" ")
        if RIGHT not in display.neighbors:
            break
        display = display.neighbors[RIGHT]
    print("")
    if BOTTOM not in top_left_corner.neighbors:
        break
    top_left_corner = top_left_corner.neighbors[BOTTOM]
# graph = build_contact_graph(raw_input)
# analyze_graph(graph)
