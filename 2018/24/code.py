import re
from collections import defaultdict
from operator import itemgetter, attrgetter

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


class Group:
    counter = 0

    def __init__(self, desc, side):
        Group.counter += 1
        self.side = side
        self.id = f"{side}-{Group.counter}"
        first_regex = re.compile(
            r"(?P<nb_units>\d+) units each with (?P<hp>\d+) hit points.+with an attack that does (?P<attack>\d+) (?P<attack_type>\w+) damage at initiative (?P<initiative>\d+)"
        )
        match = first_regex.match(desc)
        self.units = int(match.group("nb_units"))
        self.hp = int(match.group("hp"))
        self.attack_amount = int(match.group("attack"))
        self.attack_type = match.group("attack_type")
        self.initiative = int(match.group("initiative"))
        self.targeted = False
        self.target = None

        immune_regex = re.compile("immune to (?P<immunity>[^;)]+)+[;)]")
        immune_match = immune_regex.search(desc)
        if immune_match:
            self.immune_to = immune_match.group("immunity").split(", ")
        else:
            self.immune_to = []

        weak_regex = re.compile("weak to (?P<weakness>[^;)]+)+[;)]")
        weakness_match = weak_regex.search(desc)
        if weakness_match:
            self.weak_to = weakness_match.group("weakness").split(", ")
        else:
            self.weak_to = []
        self.compute_effective_power()

    def compute_effective_power(self):
        self.effective_power = self.units * self.attack_amount

    def potential_damage_from(self, other_group):
        if self.targeted == True:
            return 0
        return self.actual_damage_from(other_group)

    def actual_damage_from(self, other_group):
        if (
            self.units == 0
            or self.side == other_group.side
            or other_group.attack_type in self.immune_to
        ):
            return 0
        damage = other_group.effective_power
        if other_group.attack_type in self.weak_to:
            damage *= 2
        return damage

    def attack(self, target):
        if target is None:
            return
        if self.effective_power == 0:
            return
        damage = target.actual_damage_from(self)
        # print(f"group {self} attacks {target}")
        total_target_hp = target.units * target.hp
        if total_target_hp <= damage:
            # print(f"  {target.units} killed")
            target.units = 0
            target.compute_effective_power()
            # print(f"  target {target} is destroyed")
            return
        units_killed = damage // target.hp
        target.units -= units_killed
        target.compute_effective_power()
        # print(f"  {units_killed} killed")
        # print(f"  {target.units} remaining in {target}")

    def __str__(self):
        return f"{self.id} / HP {self.hp} / units {self.units} / Power {self.effective_power}"


class Army:
    name = ""
    groups = []

    def __init__(self, name):
        self.name = name

    def add_group(self, desc, side):
        self.groups.append(Group(desc, side))

    def targeting_phase(army):
        army.groups.sort(key=attrgetter("effective_power", "initiative"), reverse=True)
        for group in army.groups:
            target = max(army.groups, key=lambda g: g.potential_damage_from(group))
            if target.potential_damage_from(group) > 0:
                group.target = target
                target.targeted = True
                # print(f"{group} targets {target}")

    def attack_phase(army):
        army.groups.sort(key=attrgetter("initiative", "effective_power"), reverse=True)
        for group in army.groups:
            if group.target:
                group.attack(group.target)
                group.target.targeted = False
                group.target = None

    def counting_groups(self):
        d = defaultdict(lambda: 0)
        for group in self.groups:
            d[group.side] += group.units
        return d


def tests_groups():

    g1 = Group(
        "543 units each with 2286 hit points with an attack that does 34 cold damage at initiative 13",
        1,
    )
    u.assert_equals(g1.units, 543)
    u.assert_equals(g1.hp, 2286)
    u.assert_equals(g1.attack_amount, 34)
    u.assert_equals(g1.attack_type, "cold")
    u.assert_equals(g1.initiative, 13)
    u.assert_equals(g1.effective_power, 18462)

    g2 = Group(
        "688 units each with 1749 hit points (immune to slashing, radiation) with an attack that does 23 cold damage at initiative 7",
        1,
    )
    u.assert_equals(g2.units, 688)
    u.assert_equals(g2.hp, 1749)
    u.assert_equals(g2.attack_amount, 23)
    u.assert_equals(g2.attack_type, "cold")
    u.assert_equals(g2.initiative, 7)
    u.assert_equals(g2.immune_to, ["slashing", "radiation"])

    g3 = Group(
        "47 units each with 4241 hit points (weak to slashing, cold; immune to radiation) with an attack that does 889 cold damage at initiative 10",
        1,
    )
    u.assert_equals(g3.immune_to, ["radiation"])
    u.assert_equals(g3.weak_to, ["slashing", "cold"])


tests_groups()


def fight(raw_input):
    army = Army("Example 1")
    side = "Immune System"
    for row in filter(None, raw_input.splitlines()):
        if row == "Immune System:":
            side = "Immune System"
        elif row == "Infection:":
            side = "Infection"
        else:
            army.add_group(row, side)
            counted_groups = dict(army.counting_groups())

    counted_groups = dict(army.counting_groups())
    # print(counted_groups)
    for i in range(1000):
        army.targeting_phase()
        army.attack_phase()
        counted_groups = dict(army.counting_groups())
        # print(counted_groups)
        if 0 in counted_groups.values():
            break
    return max(counted_groups.values())


u.assert_equals(fight(example), 5216)

u.answer_part_1(fight(raw_input))
# 30454 too high
# 25241 too high
# 25241 again
# 23385 !

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
