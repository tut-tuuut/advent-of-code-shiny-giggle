import networkx as nx
from collections import deque, namedtuple

import utils as u

BOSS_HP = 55
BOSS_DAMAGE = 8

V = "VICTORY"
D = "DEFEAT"

my_input = """Hit Points: 55
Damage: 8"""

Situation = namedtuple(
    "Situation",
    "player_turn spent_mp boss_hp player_hp player_mp shield_timer poison_timer recharge_timer cast_spells",
)


def find_neighbor_situations(situation: Situation):

    # 0. Check victory/defeat
    if situation.boss_hp <= 0:
        return []
    if situation.player_hp <= 0:
        return []

    # 1. apply effects
    boss_hp = situation.boss_hp
    player_hp = situation.player_hp
    if situation.player_turn:
        player_hp -= 1
        if situation.player_hp <= 0:
            return []
    player_mp = situation.player_mp
    player_armor = 0
    if situation.poison_timer > 0:
        boss_hp -= 3
    if situation.shield_timer > 0:
        player_armor = 7
    if situation.recharge_timer > 0:
        player_mp += 101

    if player_mp < 53:  # if the player cannot cast any spell, they lose
        return []
    if boss_hp <= 0:  # if the boss is dead by poison, it's a victory
        return []

    # prepare timers for next turn
    next_timers = (
        max(0, situation.shield_timer - 1),
        max(0, situation.poison_timer - 1),
        max(0, situation.recharge_timer - 1),
    )

    # 2.a Player turn
    if situation.player_turn and player_mp >= 53:
        # Magic Missile : costs 53 mana, does 4 damage instantly
        if player_mp >= 53:
            yield Situation(
                False,
                situation.spent_mp + 53,
                boss_hp - 4,
                player_hp,
                player_mp - 53,
                *next_timers,
                situation.cast_spells + " missile",
            )

        # Drain : costs 73 mana. Instantly does 2 damage and heals player 2 HP
        if player_mp >= 73:
            yield Situation(
                False,
                situation.spent_mp + 73,
                boss_hp - 2,
                player_hp + 2,
                player_mp - 73,
                *next_timers,
                situation.cast_spells + " drain",
            )

        # Shield : costs 113 mana, starts "shield" effect for 6 turns
        if player_mp >= 113 and situation.shield_timer == 0:
            yield Situation(
                False,
                situation.spent_mp + 113,
                boss_hp,
                player_hp,
                player_mp - 113,
                6,
                *next_timers[1:],
                situation.cast_spells + " shield",
            )

        # Poison : 173 mana, starts "poison" effect for 6 turns
        if player_mp >= 173 and situation.poison_timer == 0:
            yield Situation(
                False,
                situation.spent_mp + 173,
                situation.boss_hp,
                player_hp,
                player_mp - 173,
                next_timers[0],
                6,
                next_timers[2],
                situation.cast_spells + " poison",
            )

        # Recharge : 229 mana, starts "recharge" effect for 5 turns
        if player_mp >= 229 and situation.recharge_timer == 0:
            yield Situation(
                False,
                situation.spent_mp + 229,
                situation.boss_hp,
                player_hp,
                player_mp - 229,
                *next_timers[:-1],
                5,
                situation.cast_spells + " recharge",
            )

    # 2.b. Boss’ turn
    if boss_hp > 0 and not situation.player_turn:
        damage = max(1, BOSS_DAMAGE - player_armor)
        yield Situation(
            True,
            situation.spent_mp,
            boss_hp,
            player_hp - damage,
            player_mp,
            *next_timers,
            situation.cast_spells + " •",
        )


def debug_situation(s: Situation):
    if type(s) == str:
        print(s)
        return

    print(f"😈{s.boss_hp} 🧙‍{s.player_hp} 📘{s.player_mp} ", end="")
    if s.shield_timer > 0:
        print(f"🛡 {s.shield_timer} ", end="")
    if s.poison_timer > 0:
        print(f"🐍{s.poison_timer} ", end="")
    if s.recharge_timer > 0:
        print(f"✨{s.recharge_timer} ", end="")
    print("")


def is_victory(s: Situation):
    # 0. Check victory/defeat
    if situation.boss_hp <= 0:
        return V
    if situation.player_turn and situation.player_hp <= 1:
        return D
    if not situation.player_turn and situation.player_hp <= 0:
        return D

    # 1. apply effects
    boss_hp = situation.boss_hp
    player_mp = situation.player_mp
    if situation.poison_timer > 0:
        boss_hp -= 3
        if boss_hp <= 0:  # if the boss is dead by poison, it's a victory
            return V

    if situation.recharge_timer > 0:
        player_mp += 101
    if player_mp < 53:  # if the player cannot cast any spell, they lose
        return D


# Part 2 ---------------------------------------------------

initial_situation = Situation(True, 0, 55, 50, 500, 0, 0, 0, "")

todo_list = deque()
todo_list.append(initial_situation)
print(f"{len(todo_list)} in todo list")
cheapest_victory_cost = 999999

for i in range(5555555):
    try:
        situation = todo_list.pop()
    except IndexError:
        print(f"todo list is empty at iteration {i}")
        break
    if situation.spent_mp > cheapest_victory_cost:
        continue
    if is_victory(situation) == V:
        if situation.spent_mp < cheapest_victory_cost:
            print(situation.cast_spells)
            cheapest_victory_cost = situation.spent_mp
            print(f"cheapest victory cost: {cheapest_victory_cost}")
            print("---------")
        continue
    elif is_victory == D:
        continue
    for next_situation in find_neighbor_situations(situation):
        todo_list.append(next_situation)

u.assert_equals(cheapest_victory_cost, 1289)  # cf pompage.py

u.answer_part_2(cheapest_victory_cost)
# 1408 too high 296455 iterations
# 1295 too high 4563918 iterations, I keep finding this one
# 847 too low 2980515 iterations
# 900 WRONG 4230201 iterations
# 1295:
# recharge • poison • shield • missile • missile • recharge • poison • shield • missile • missile • missile
# 1289:
# Poison -> Magic Missile -> Recharge -> Poison -> Shield -> Recharge -> Poison -> Drain -> Drain