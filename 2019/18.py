import networkx as nx
from collections import namedtuple

Point = namedtuple("Point", "x y type name")


def parse_map(strMap):
    rows = strMap.split("\n")
    grid = {}
    graphRow = nx.Graph()
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            coords = f"{x}-{y}"
            if char == "#":
                continue
            if char in "azertyuiopqsdfghjklmwxcvbn":
                type = "key"
            elif char in "AZERTYUIOPQSDFGHJKLMWXCVBN":
                type = "door"
            elif char == "@":
                type = "entrance"
            elif char == ".":
                type = "."


def sandbox():
    map1 = """#########
#b.A.@.a#
#########"""  # 8 steps

    parse_map(map1)

    map2 = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""  # 86 steps (take d before e)

    map3 = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""  # 132 steps: b, a, c, d, f, e, g

    map4 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""  # 136 steps - one is a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m

    map5 = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""  # 81 steps; one is: a, c, f, i, d, g, b, e, h


sandbox()
