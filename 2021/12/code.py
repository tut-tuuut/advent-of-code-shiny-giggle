import utils as u
import re
import networkx as nx

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_10paths = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

example_19paths = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

example_226paths = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


class PathFinder:
    SMALL_REGEX = re.compile(r"[a-z]+")

    def __init__(self, raw_input):
        self.graph = nx.Graph()
        self.graph.add_edges_from(
            tuple(row.split("-")) for row in raw_input.splitlines()
        )
        self.paths = set()

    def find_all_paths(self):
        self.visit("start", [])
        return len(self.paths)

    def finished_path(self, path):
        self.paths.add(tuple(path))

    def is_small(self, node):
        return bool(self.SMALL_REGEX.match(node))

    def visit(self, node, path):
        path.append(node)
        if node == "end":
            self.finished_path(path)
            return
        for neighbor in nx.neighbors(self.graph, node):
            if neighbor in path and self.is_small(neighbor):
                continue
            self.visit(neighbor, path.copy())


pf = PathFinder(example_10paths)
u.assert_equals(pf.find_all_paths(), 10)

pf = PathFinder(example_19paths)
u.assert_equals(pf.find_all_paths(), 19)

pf = PathFinder(example_226paths)
u.assert_equals(pf.find_all_paths(), 226)

pf = PathFinder(raw_input)
u.answer_part_1(pf.find_all_paths())

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


class ImprovedPathFinder(PathFinder):
    def visit(self, node, path, one_small_cave_visited_twice=False):
        path.append(node)
        if node == "end":
            self.finished_path(path)
            return
        for neighbor in nx.neighbors(self.graph, node):
            if neighbor == "start":
                continue
            if (
                one_small_cave_visited_twice
                and neighbor in path
                and self.is_small(neighbor)
            ):
                continue
            elif (
                not one_small_cave_visited_twice
                and neighbor in path
                and self.is_small(neighbor)
            ):
                self.visit(neighbor, path.copy(), True)
                continue
            self.visit(neighbor, path.copy(), one_small_cave_visited_twice)


pf = ImprovedPathFinder(example_10paths)
u.assert_equals(pf.find_all_paths(), 36)

pf = ImprovedPathFinder(example_19paths)
u.assert_equals(pf.find_all_paths(), 103)

pf = ImprovedPathFinder(example_226paths)
u.assert_equals(pf.find_all_paths(), 3509)

pf = ImprovedPathFinder(raw_input)
u.answer_part_2(pf.find_all_paths())
