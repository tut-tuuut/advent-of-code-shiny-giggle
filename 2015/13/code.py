import utils as u
import networkx as nx
import re

parseRegex = r'^(\w+)\s.*(gain|lose)\s(\d+)\s.*\s(\w+)\.$'
regex = re.compile(parseRegex, re.MULTILINE)
# https://regex101.com/r/SX25wx/1/

def buildGraphFromInputString(inputStr):
    graph = nx.Graph()
    info = regex.findall(inputStr)
    for row in info:
        person1, sign, amount, person2 = row
        if sign == 'lose':
            amount = -1 * int(amount)
        elif sign == 'gain':
            amount = int(amount)
        graph.add_node(person1)
        graph.add_node(person2)
        amount = amount + graph.get_edge_data(person1, person2, {'happiness': 0})['happiness']
        graph.add_edge(person1, person2, happiness=amount)
    return graph

class HappinessOptimizer:
    def __init__(self, graph):
        self.graph = graph
        self.graphLen = len(graph.nodes)
        self.maxHappiness = 0
        self.optimumPlacement = []

    def findOptimalHappiness(self):
        for node in self.graph.nodes:
            path = []
            self.visit(node, path)
        return self.maxHappiness

    def visit(self, node, path):
        path.append(node)
        if len(path) == self.graphLen:
            self.analyzePlacement(path)
            return
        for n in nx.neighbors(graph, node):
            if n in path:
                continue
            self.visit(n, path.copy())

    def analyzePlacement(self, path):
        happiness = nx.path_weight(self.graph, path, 'happiness')
        happiness = happiness + self.graph.get_edge_data(path[0], path[-1])['happiness']
        if happiness > self.maxHappiness:
            self.maxHappiness = happiness
            self.optimumPlacement = path

example = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

graph = buildGraphFromInputString(example)
ho = HappinessOptimizer(graph)

u.assert_equals(ho.findOptimalHappiness(), 330)

with open(__file__+'.input.txt', "r+") as file:
    inputStr = file.read()
    graph = buildGraphFromInputString(inputStr)
    ho = HappinessOptimizer(graph)
    u.answer_part_1(ho.findOptimalHappiness())

    graph = graph.copy()
    guests = list(graph.nodes)
    for n in guests:
        graph.add_edge(n, 'Me', happiness=0)
    
    ho = HappinessOptimizer(graph)
    u.answer_part_2(ho.findOptimalHappiness())
