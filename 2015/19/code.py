import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()


molecule_pattern = re.compile(r"\n(\w+)\n", re.M)
molecule = molecule_pattern.search(inputStr).group(1)


replacement_pattern = re.compile(r"\b(\w+) => (\w+)\b")
replacements = replacement_pattern.findall(inputStr)


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
example_replacements = (("H", "HO"), ("H", "OH"), ("O", "HH"))

print(find_all_resulting_molecules(example_molecule, example_replacements))

u.answer_part_1(len(find_all_resulting_molecules(molecule, replacements)))