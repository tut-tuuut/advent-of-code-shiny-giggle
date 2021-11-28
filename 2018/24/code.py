import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


class Group:
    units = 0
    hp = 0
    attack_amount = 0
    attack_type = ""
    initiative = 0
    weak_to = []
    immune_to = []

    def __init__(self, desc):
        # 18 units each with 729 hit points (weak to fire; immune to cold, slashing)
        # with an attack that does 8 radiation damage at initiative 10
        first_regex = re.compile(
            r"(?P<nb_units>\d+) units each with (?P<hp>\d+) hit points.+with an attack that does (?P<attack>\d+) (?P<attack_type>\w+) damage at initiative (?P<initiative>\d+)"
        )
        match = first_regex.match(desc)
        self.units = int(match.group("nb_units"))
        self.hp = int(match.group('hp'))
        self.attack_amount = int(match.group('attack'))
        self.attack_type = match.group('attack_type')
        self.initiative = int(match.group('initiative'))

        immune_regex = re.compile("immune to (?P<immunity>[^;)]+)+[;)]")
        immune_match = immune_regex.search(desc)
        if immune_match:
            self.immune_to = immune_match.group('immunity').split(', ')

        weak_regex = re.compile("weak to (?P<weakness>[^;)]+)+[;)]")
        weakness_match = weak_regex.search(desc)
        if weakness_match:
            self.weak_to = weakness_match.group('weakness').split(', ')


g1 = Group(
    "543 units each with 2286 hit points with an attack that does 34 cold damage at initiative 13"
)
u.assert_equals(g1.units, 543)
u.assert_equals(g1.hp, 2286)
u.assert_equals(g1.attack_amount, 34)
u.assert_equals(g1.attack_type, "cold")
u.assert_equals(g1.initiative, 13)

g2 = Group(
    "688 units each with 1749 hit points (immune to slashing, radiation) with an attack that does 23 cold damage at initiative 7"
)
u.assert_equals(g2.units, 688)
u.assert_equals(g2.hp, 1749)
u.assert_equals(g2.attack_amount, 23)
u.assert_equals(g2.attack_type, "cold")
u.assert_equals(g2.initiative, 7)
u.assert_equals(g2.immune_to, ['slashing', 'radiation'])

g3 = Group(
    "47 units each with 4241 hit points (weak to slashing, cold; immune to radiation) with an attack that does 889 cold damage at initiative 10"
)
u.assert_equals(g3.immune_to, ['radiation'])
u.assert_equals(g3.weak_to, ['slashing', 'cold'])

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
