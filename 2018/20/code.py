import networkx as nx
from collections import deque
from PIL import Image, ImageDraw
from time import time

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

examples = {
    "^WNE$": 3,
    "^ENWWW(NEEE|SSE(EE|N))$": 10,
    "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$": 18,
    "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$": 23,
    "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$": 31,
}

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def build_map_from_regex(regex):
    map = nx.Graph()
    x, y = 0, 0  # initial position
    crossways = deque()
    for char in regex:
        if char == "W":
            map.add_edge((x - 1, y), (x, y))
            x -= 1
        elif char == "E":
            map.add_edge((x + 1, y), (x, y))
            x += 1
        elif char == "N":
            map.add_edge((x, y - 1), (x, y))
            y -= 1
        elif char == "S":
            map.add_edge((x, y + 1), (x, y))
            y += 1
        elif char == "(":
            crossways.append((x, y))
        elif char == ")":
            x, y = crossways.pop()
        elif char == "|":
            x, y = crossways[-1]
        elif char == "^":
            pass
        elif char == "$":
            pass
    return map


def calculate_shortest_paths(map: nx.Graph):
    return {z: -1 + len(nx.shortest_path(map, z, (0, 0))) for z in map.nodes()}


def draw_map(map: nx.Graph):
    min_x = min(x for x, y in map.nodes())
    max_x = max(x for x, y in map.nodes())
    min_y = min(y for x, y in map.nodes())
    max_y = max(y for x, y in map.nodes())
    w = 11  # size of a room
    s = 2 * w + 4  # space between two squares

    room_color = (200, 200, 200)
    imgFile = Image.new(
        "RGB", (s * (1 + max_x - min_x), s * (1 + max_y - min_y)), (0, 0, 0)
    )
    drawing = ImageDraw.Draw(imgFile)

    def fix_x(x: int):
        return (x - min_x) * s + int(s / 2)

    def fix_y(y: int):
        return (y - min_y) * s + int(s / 2)

    # ImageDraw.regular_polygon
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.regular_polygon
    for x, y in map.nodes():
        drawing.regular_polygon((fix_x(x), fix_y(y), w), 4, fill=room_color)
    for a, b in map.edges():
        xa, ya = a
        xb, yb = b
        drawing.line(
            (fix_x(xa), fix_y(ya), fix_x(xb), fix_y(yb)), fill=room_color, width=3
        )
    drawing.regular_polygon((fix_x(0), fix_y(0) + 1, w - 3), 3, fill=(200, 0, 0))

    imgFile.show()


for regex, expected in examples.items():
    map = build_map_from_regex(regex)
    path_lengths = calculate_shortest_paths(map)
    u.assert_equals(max(path_lengths.values()), expected)

map = build_map_from_regex(raw_input)
draw_map(map)  # whoa, this place is HUGE indeed

print(f"calculating path lengths...")
init_time = time()
path_lengths = calculate_shortest_paths(map)
print(f"Done! It took {time() - init_time:.2f} seconds.")

max_length = max(path_lengths.values())
u.assert_equals(max_length, 3885)
u.answer_part_1(max_length)  # 3885

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.answer_part_2(sum(1 for length in path_lengths.values() if length >= 1000))
