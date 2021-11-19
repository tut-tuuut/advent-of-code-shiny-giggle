import networkx as nx
from collections import deque, namedtuple

import utils as u

BOSS_HP = 55
BOSS_DAMAGE = 8

V = "VICTORY"
D = "DEFEAT"

my_input = """Hit Points: 55
Damage: 8"""

"""
On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

    Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
    At the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the player's
turns and the boss' turns. Effects are created with a timer (the number of turns they last);
at the start of each turn, after they apply any effect they have, their timer is decreased by one.
If this decreases the timer to zero, the effect ends.
You cannot cast a spell that would start an effect which is already active.
However, effects can be started on the same turn they end.
"""

Situation = namedtuple(
    "Situation",
    "player_turn spent_mp boss_hp player_hp player_mp shield_timer poison_timer recharge_timer",
)


def find_neighbor_situations(situation: Situation):

    # debug_situation(situation)

    if type(situation) == str:
        return []
    # 0. Check victory/defeat
    if situation.boss_hp <= 0:
        return []
    if situation.player_hp <= 0:
        return []

    # 1. apply effects
    boss_hp = situation.boss_hp
    player_hp = situation.player_hp
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
    if situation.player_hp <= 0:
        return D

    # 1. apply effects
    boss_hp = situation.boss_hp
    player_hp = situation.player_hp
    player_mp = situation.player_mp
    player_armor = 0
    if situation.poison_timer > 0:
        boss_hp -= 3
    if situation.shield_timer > 0:
        player_armor = 7
    if situation.recharge_timer > 0:
        player_mp += 101

    if player_mp < 53:  # if the player cannot cast any spell, they lose
        return D
    if boss_hp <= 0:  # if the boss is dead by poison, it's a victory
        return V


# Part 1 ---------------------------------------------------

initial_situation = Situation(True, 0, 55, 50, 500, 0, 0, 0)

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
            cheapest_victory_cost = situation.spent_mp
            print(f"cheapest victory cost: {cheapest_victory_cost}")
        continue
    elif is_victory == D:
        continue
    for next_situation in find_neighbor_situations(situation):
        todo_list.append(next_situation)

u.answer_part_1(cheapest_victory_cost)
# 1664 too high
# 1368 too high
# 953 found with 5555555 iterations
