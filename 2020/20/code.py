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


def find_corner_tiles(raw_tileset):
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
