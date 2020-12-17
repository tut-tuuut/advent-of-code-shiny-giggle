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
    "player_turn boss_hp player_hp player_mp shield_timer poison_timer recharge_timer",
)


def add_neighbor_situations(situation: Situation, g: nx.DiGraph):

    # debug_situation(situation)

    if type(situation) == str:
        return
    # 0. Check victory/defeat
    if situation.player_hp <= 1:
        g.add_edge(situation, D, cost=0)
        return
    if situation.boss_hp <= 0:
        g.add_edge(situation, V, cost=0)
        return
    minimum_needed_to_not_lose = 0
    if situation.player_turn:
        minimum_needed_to_not_lose = 1

    # 1. apply effects
    boss_hp = situation.boss_hp
    if not situation.player_turn:
        boss_hp -= 1
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
        g.add_edge(situation, D, cost=0)
        return
    if boss_hp <= 0:  # if the boss is dead by poison, it's a victory
        g.add_edge(situation, V, cost=0)
        return

    # prepare timers for next turn
    next_timers = (
        max(0, situation.shield_timer - 1),
        max(0, situation.poison_timer - 1),
        max(0, situation.recharge_timer - 1),
    )

    # 2.a Player turn
    if situation.player_turn and player_mp >= 53:
        player_hp -= 1  # hard mode

        # Magic Missile : costs 53 mana, does 4 damage instantly
        if player_mp >= 53:
            next_situation = Situation(
                False, boss_hp - 4, player_hp, player_mp - 53, *next_timers
            )
            g.add_edge(situation, next_situation, cost=53)

        # Drain : costs 73 mana. Instantly does 2 damage and heals player 2 HP
        if player_mp >= 73:
            next_situation = Situation(
                False, boss_hp - 2, player_hp + 2, player_mp - 73, *next_timers
            )
            g.add_edge(situation, next_situation, cost=73)

        # Shield : costs 113 mana, starts "shield" effect for 6 turns
        if player_mp >= 113 and situation.shield_timer == 0:
            next_situation = Situation(
                False, boss_hp, player_hp, player_mp - 113, 6, *next_timers[1:]
            )
            g.add_edge(situation, next_situation, cost=113)

        # Poison : 173 mana, starts "poison" effect for 6 turns
        if player_mp >= 173 and situation.poison_timer == 0:
            next_situation = Situation(
                False,
                situation.boss_hp,
                player_hp,
                player_mp - 173,
                next_timers[0],
                6,
                next_timers[2],
            )
            g.add_edge(situation, next_situation, cost=173)

        # Recharge : 229 mana, starts "recharge" effect for 5 turns
        if player_mp >= 229 and situation.recharge_timer == 0:
            next_situation = Situation(
                False,
                situation.boss_hp,
                player_hp,
                player_mp - 229,
                *next_timers[:-1],
                5,
            )
            g.add_edge(situation, next_situation, cost=229)

    # 2.b. Boss’ turn
    if boss_hp > 0 and not situation.player_turn:
        damage = max(1, BOSS_DAMAGE - player_armor)
        next_situation = Situation(
            True, boss_hp, player_hp - damage, player_mp, *next_timers
        )
        g.add_edge(situation, next_situation, cost=0)


def debug_situation(s: Situation):
    if type(s) == str:
        print(s)
        return
    if s.player_turn:
        print("P ", end="")
    else:
        print("B ", end="")
    print(f"😈{s.boss_hp} 🧙‍{s.player_hp} 📘{s.player_mp} ", end="")
    if s.shield_timer > 0:
        print(f"🛡 {s.shield_timer} ", end="")
    if s.poison_timer > 0:
        print(f"🐍{s.poison_timer} ", end="")
    if s.recharge_timer > 0:
        print(f"✨{s.recharge_timer} ", end="")
    print("")


# Part 2 ---------------------------------------------------

initial_situation = Situation(True, 55, 50, 500, 0, 0, 0)

graph = nx.DiGraph()
graph.add_node(V)
graph.add_node(D)

todo_list = deque()
todo_list.append(initial_situation)
print(f"{len(todo_list)} in todo list")

for i in range(5555555):
    # print(f"{i:02d} -----------")
    try:
        situation = todo_list.pop()
    except IndexError:
        print(f"todo list is empty at iteration {i}")
        break
    add_neighbor_situations(situation, graph)
    for next_situation in graph.successors(situation):
        todo_list.append(next_situation)
    # print(f"{len(todo_list)} in todo list")
    # print(f"{len(list(graph.predecessors(V)))} victories found")
    # print(f"{len(list(graph.predecessors(D)))} defeats found")

print(f"{len(list(graph.predecessors(V)))} victories found!")
cheapest_path = nx.dijkstra_path(graph, initial_situation, V, weight="cost")
for situation in cheapest_path:
    debug_situation(situation)

u.answer_part_2(nx.path_weight(graph, cheapest_path, "cost"))
# 1408 too high 296455 iterations
# 1295 too high 4563918 iterations
# 847 too low 2980515 iterations
# 900 WRONG 4230201 iterations