import re
from itertools import count
from operator import attrgetter

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
            return 0
        if self.effective_power == 0:
            return 0
        damage = target.actual_damage_from(self)
        # print(f"group {self} attacks {target}")
        total_target_hp = target.units * target.hp
        if total_target_hp <= damage:
            killed = target.units
            target.units = 0
            target.compute_effective_power()
            # print(f"  target {target} is destroyed")
            return killed
        units_killed = damage // target.hp
        target.units -= units_killed
        target.compute_effective_power()
        return units_killed
        # print(f"  {units_killed} killed")
        # print(f"  {target.units} remaining in {target}")

    def __str__(self):
        return f"{self.id} / HP {self.hp} / units {self.units} / Power {self.effective_power}"


class Army:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def add_group(self, desc, side):
        self.groups.append(Group(desc, side))

    def targeting_phase(army):
        army.groups.sort(key=attrgetter("effective_power", "initiative"), reverse=True)
        for group in army.groups:
            max_damage = max(g.potential_damage_from(group) for g in army.groups)
            if max_damage == 0:
                next
            potential_targets = [
                g for g in army.groups if max_damage == g.potential_damage_from(group)
            ]
            max_power = max(g.effective_power for g in potential_targets)
            potential_targets = [
                g for g in potential_targets if g.effective_power == max_power
            ]
            potential_targets.sort(key=attrgetter("initiative"), reverse=True)
            # if len(potential_targets) > 1:
            # print([str(t) for t in potential_targets])
            target = potential_targets[0]
            if target.potential_damage_from(group) > 0:
                group.target = target
                target.targeted = True
                # print(f"{group} targets {target}")

    def attack_phase(army):
        something_happened = False
        army.groups.sort(key=attrgetter("initiative", "effective_power"), reverse=True)
        for group in army.groups:
            if group.target:
                units_killed = group.attack(group.target)
                group.target.targeted = False
                group.target = None
                if units_killed > 0:
                    something_happened = True
        return something_happened

    def cleaning_phase(self):
        for group in self.groups:
            group.compute_effective_power()
        self.groups = [g for g in self.groups if g.effective_power > 0]

    def counting_groups(self):
        d = {"Infection": 0, "Immune System": 0}
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
    for i in range(10000):
        # print(f"------ ROUND {i} -----------")
        army.targeting_phase()
        something_happened = army.attack_phase()
        counted_groups = dict(army.counting_groups())
        if not something_happened:
            print("nothing happens")
            break
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


def boosted_fight(input_str, boost):
    army = Army(f"xxxx")
    side = "Immune System"
    for row in filter(None, input_str.splitlines()):
        if row == "Immune System:":
            side = "Immune System"
        elif row == "Infection:":
            side = "Infection"
        else:
            army.add_group(row, side)
            counted_groups = dict(army.counting_groups())
    for group in army.groups:
        if group.side == "Immune System":
            group.attack_amount += boost
            group.compute_effective_power()
    counted_groups = dict(army.counting_groups())
    for counter in count():
        army.targeting_phase()
        something_happened = army.attack_phase()
        if not something_happened:
            print("blah, nothing happened this phase")
            break
        army.cleaning_phase()
        counted_groups = dict(army.counting_groups())
        if 0 in counted_groups.values():
            print(f"phew! fight is over after {counter} rounds")
            break
    print(counted_groups)
    return max(counted_groups.values()), counted_groups["Infection"] == 0


u.assert_equals(boosted_fight(example, 0), (5216, False))
u.assert_equals(boosted_fight(example, 1570), (51, True))
u.assert_equals(boosted_fight(raw_input, 0), (23385, False))

for i in range(85, 100):
    remaining, immune_has_won = boosted_fight(raw_input, i)
    if immune_has_won:
        u.answer_part_2(f"{remaining} units with a boost of {i}")
        break

# boosted_fight(raw_input, 92)

# 3516 too high with boost 92
# 2344 units with boost 88 ?
