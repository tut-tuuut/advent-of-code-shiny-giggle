import re
from collections import deque

import networkx as nx

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()


molecule_pattern = re.compile(r"\n(\w+)\n", re.M)
molecule = molecule_pattern.search(inputStr).group(1)


replacement_pattern = re.compile(r"\b(\w+) => (\w+)\b")
replacements = replacement_pattern.findall(inputStr)
# sort replacements with "heaviest" first, it will be useful for part 2
replacements = sorted(replacements, key=lambda x: -len(x[1]))

# Part 1 ------------------------------------------------------------------


def find_all_resulting_molecules(molecule, replacements):
    resulting_molecules = set()
    for mol_from, mol_to in replacements:
        for index in [m.start() for m in re.finditer(mol_from, molecule)]:
            new_molecule = molecule[:index] + molecule[index:].replace(
                mol_from, mol_to, 1
            )
            resulting_molecules.add(new_molecule)
    return resulting_molecules


example_molecule = "HOH"
example_replacements = (("H", "HO"), ("H", "OH"), ("O", "HH"), ("e", "H"), ("e", "O"))

print(find_all_resulting_molecules(example_molecule, example_replacements))

u.answer_part_1(len(find_all_resulting_molecules(molecule, replacements)))

#
#                         _\/_
#                          /\
#                          /\
#                         /  \
#                         /~~\o
#       PART    ------   /o   \  ------  TWO
#                       /~~*~~~\
#                      o/    o \
#                      /~~~~~~~~\~`
#                     /__*_______\
#                          ||
#                        \====/
#                         \__/
#

# the problem in part 2 is absolutely NOTHING LIKE the first part...
# Try a width-first search?
# Or we could start from target_molecule and try to reduce it to e?
# Just use replacements in the other order...


def reduce_molecule(target_molecule, replacements):
    """Use a nx.DiGraph() to find the shortest path between target_molecule and e"""
    # First, build the graph --------------------------
    graph = nx.DiGraph()
    molecules_to_reduce = deque([target_molecule])
    examined_molecules = set()  # to avoid examining molecules twice
    shortest_molecule_achieved = len(target_molecule) + 3  # to be more efficient
    i = 0
    while len(molecules_to_reduce) > 0:
        i += 1
        molecule = molecules_to_reduce.pop()
        if len(molecule) > shortest_molecule_achieved + 15:
            # avoid molecules which are REALLY longer than what we already have
            continue
        examined_molecules.add(molecule)
        max_reducing_factor = 0
        for mol_from, mol_to in replacements:
            # ↑ replacements are sorted from the most efficient to the less efficient,
            # to first check the combinations which have a greater chance to remove a lot
            # of characters.
            for index in [m.start() for m in re.finditer(mol_to, molecule)]:
                new_molecule = molecule[:index] + molecule[index:].replace(
                    mol_to,  # reversed vs. part 1 (mol_to replaced with mol_from)
                    mol_from,
                    1,
                )
                graph.add_edge(molecule, new_molecule)
                if new_molecule not in examined_molecules:
                    if len(new_molecule) <= shortest_molecule_achieved:
                        # hm! short molecule! interesting!
                        # we append on the right, to pick it first later
                        shortest_molecule_achieved = len(new_molecule)
                        molecules_to_reduce.append(new_molecule)
                        continue
                    # in that case, the molecule may be less interesting to examine,
                    # we append on the other side
                    molecules_to_reduce.appendleft(new_molecule)

    # And now the answer we're looking for: -------------------------
    # In the new graph, look for the shortest path between target and the electron.
    # It's almost too easy with networkx. (The hard part was to build the graph, though)
    return -1 + len(nx.shortest_path(graph, target_molecule, "e"))


u.assert_equals(reduce_molecule("HOH", example_replacements), 3)
u.assert_equals(reduce_molecule("HOHOHO", example_replacements), 6)

u.answer_part_2(reduce_molecule(molecule, replacements))
