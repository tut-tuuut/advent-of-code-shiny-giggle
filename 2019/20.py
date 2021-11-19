import networkx as nx


def coords(x, y):
    return f"{x}-{y}"


def parse_part1(strInput):
    grid = list(map(list, strInput.split("\n")))
    graph = nx.Graph()
    opens = {"left": [], "top": [], "right": [], "bottom": []}
    for y, row in enumerate(grid):
        for x, char in enumerate(list(row)):
            if char != ".":
                continue
            graph.add_node(coords(x, y))
            if grid[y - 1][x] == ".":  # top
                print(f"{coords(x,y)}-{coords(x,y-1)}")
                graph.add_edge(coords(x, y), coords(x, y - 1))
            elif grid[y - 1][x] != "#":
                opens["top"].append((x, y))
                print(f"{x}-{y} is open on the top")
            if grid[y][x - 1] == ".":  # left
                graph.add_edge(coords(x, y), coords(x - 1, y))
            elif grid[y][x - 1] != "#":
                opens["left"].append((x, y))
                print(f"{x}-{y} is open on the left")
            if grid[y + 1][x] not in (".", "#"):  # bottom
                opens["bottom"].append((x, y))
                print(f"{x}-{y} is open on the bottom")
            if grid[y][x + 1] not in (".", "#"):  # right
                opens["right"].append((x, y))
                print(f"{x}-{y} is open on the right")
    teleports = {}
    for o in opens["top"]:
        x, y = o
        name = f"{grid[y-2][x]}{grid[y-1][x]}"
        if name in teleports.keys():
            graph.add_edge(coords(x, y), teleports[name])
        else:
            teleports[name] = coords(x, y)
    for o in opens["bottom"]:
        x, y = o
        name = f"{grid[y+1][x]}{grid[y+2][x]}"
        if name in teleports.keys():
            graph.add_edge(coords(x, y), teleports[name])
        else:
            teleports[name] = coords(x, y)
    for o in opens["left"]:
        x, y = o
        name = f"{grid[y][x-2]}{grid[y][x-1]}"
        if name in teleports.keys():
            graph.add_edge(coords(x, y), teleports[name])
        else:
            teleports[name] = coords(x, y)
    for o in opens["right"]:
        x, y = o
        name = f"{grid[y][x+1]}{grid[y][x+2]}"
        if name in teleports.keys():
            graph.add_edge(coords(x, y), teleports[name])
        else:
            teleports[name] = coords(x, y)
    print(teleports)
    print(nx.shortest_path_length(graph, teleports["AA"], teleports["ZZ"]))


def sandbox():
    exampleInput = """                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               """
    parse_part1(exampleInput)


def part1():
    with open(__file__ + ".input") as file:
        parse_part1(file.read())


# sandbox()
part1()
