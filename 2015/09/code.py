import networkx as nx
import re

# example shortest route : London -> Dublin -> Belfast = 605

g = nx.Graph()

g.add_node('London')
g.add_node('Dublin')
g.add_node('Belfast')

g.add_edge('London', 'Dublin', weight = 464)
g.add_edge('London', 'Belfast', weight = 518)
g.add_edge('Dublin', 'Belfast', weight = 141)


class GraphWalker:
    def __init__(self, g):
        self.shortest_path = []
        self.shortest_path_length = 999999999
        self.longest_path = []
        self.longest_path_length = 0
        self.g = g
        self.graphLen = len(g)

    def find_shortest_and_longest_covering_path(self):
        for n in list(self.g.nodes)[:-1]:
            print(f'starting from {n}...')
            self.visit(n, list())
        print('x===========================x')
        print(f'! shortest path length: {self.shortest_path_length} !')
        print('x---------------------------x')
        print(f'! longest path length:  {self.longest_path_length} !')
        print('x===========================x')

    
    def visit(self, node, path):
        path.append(node)
        if len(path) == self.graphLen:
            self.finished_path(path)
            self.finished_path_part_two(path)
            return
        for neighbor in nx.neighbors(self.g, node):
            if neighbor in path:
                continue
            self.visit(neighbor, path.copy())
    
    def finished_path(self, path):
        length = nx.path_weight(self.g, path, 'weight')
        if length < self.shortest_path_length:
            self.shortest_path = path
            self.shortest_path_length = length

    def finished_path_part_two(self, path):
        length = nx.path_weight(self.g, path, 'weight')
        if length > self.longest_path_length:
            self.longest_path = path
            self.longest_path_length = length



gw = GraphWalker(g)

l = gw.find_shortest_and_longest_covering_path()

print(gw.shortest_path_length)
# a ----- b
# |___ c _|

g = nx.Graph()

with open(__file__+'.input.txt', "r+") as file:
    inputStr = file.read()
    for row in inputStr.split('\n'):
        start, end, length = re.match(r'(\w+) to (\w+) = (\d+)', row).groups()
        print(f'there is {length} km from {start} to {end}')
        g.add_edge(start, end, weight=int(length))
    gw = GraphWalker(g)
    gw.find_shortest_and_longest_covering_path()

# 510 is too high