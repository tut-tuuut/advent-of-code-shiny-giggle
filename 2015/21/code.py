from math import ceil

import utils as u

raw_input = """Hit Points: 109
Damage: 8
Armor: 2"""

YELLOW = "\033[93m"
RED = "\033[91m"
NORMAL = "\033[0m"
GREEN = "\033[92m"

DISPLAY_WIDTH = 50

SHOP = {
    # (atq, def) : price
    "Weapons": {
        (4, 0): 8,
        (5, 0): 10,
        (6, 0): 25,
        (7, 0): 40,
        (8, 0): 74,
    },
    "Armor": {
        (0, 1): 13,
        (0, 2): 31,
        (0, 3): 53,
        (0, 4): 75,
        (0, 5): 102,
    },
    "Rings": {
        (1, 0): 25,
        (2, 0): 50,
        (3, 0): 100,
        (0, 1): 20,
        (0, 2): 40,
        (0, 3): 80,
    },
}


def draw_progress_bar(value, max_value, avatar):
    display_val = int(value * DISPLAY_WIDTH / max_value)
    if value > max_value / 2:
        color = GREEN
    elif value < max_value / 5:
        color = RED
    else:
        color = YELLOW
    print(
        f"{avatar} "
        + color
        + ("█" * display_val).ljust(DISPLAY_WIDTH, "░")
        + NORMAL
        + f" {value}/{max_value}"
    )


class Bonhomme:
    """Generic character class. Could have named it "Character".
    But this is a French RPG: we must speak Frenglish."""

    def __init__(self, avatar, hp, attack, armor):
        self.avatar = avatar
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.armor = armor

    def take_a_gnon(self, attack):
        """Used when the bonhomme is hit by another bonhomme:
        GNON, pronounced "nion", is a very technical French term designing a punch, a slap, etc.
        (It is derived from the word "onion", apparently)
        """
        self.hp -= max(0, attack - self.armor)
        if self.hp < 0:
            print(f"💥 OVERKILL!!! 💥 {self.avatar} = 💀".center(60))
            self.hp = 0

    def display_status(self):
        draw_progress_bar(self.hp, self.max_hp, self.avatar)


def grandiose_fight(player, boss):
    """Display the fight between a player and a boss,
    with a lot of useless but beautiful visual effects."""
    round_count = 0
    while player.hp > 0 and boss.hp > 0:
        round_count += 1
        print(f" ⚡️ ROUND {round_count} ! ⚡️".center(59, "-"))
        boss.take_a_gnon(player.attack)
        if boss.hp > 0:
            player.take_a_gnon(boss.attack)
        boss.display_status()
        player.display_status()
        print("")
    if boss.hp <= 0:
        print(f" {player.avatar} WINS! VICTORY ! ".center(40, "🌟"))
    else:
        print(f" {player.avatar} HAS LOST! DEFEAT! ".center(40, "💩"))
    print("")


def poutrage_index(player, boss):
    """Poutrage index is >= 0 if the player wins, < 0 if the boss wins.
    A higer absolute value indicates a more radiant victory or a more crushing defeat.
    The French term for that is "poutrage", from the verb "poutrer" like in "j’ai poutré le boss",
    or like in "le boss m’a poutré·e", referring to the fact you could as well have used some poutres
    to win/lose the fight.
    """
    rounds_for_player_to_win = ceil(boss.hp / (player.attack - boss.armor))
    rounds_for_boss_to_win = ceil(player.hp / (boss.attack - player.armor))
    return rounds_for_boss_to_win - rounds_for_player_to_win


def stuff_player(base_player_stats, stuff_stats):
    return Bonhomme(
        base_player_stats[0],
        base_player_stats[1],
        base_player_stats[2] + sum(stat[0] for stat in stuff_stats),
        base_player_stats[3] + sum(stat[1] for stat in stuff_stats),
    )


# draw_progress_bar(60, 100, "😻")
# draw_progress_bar(10, 80, "🧚‍")
# draw_progress_bar(45, 120, "🐉")

# example_player = Bonhomme("😻", 8, 5, 5)
# example_boss = Bonhomme("🧚‍", 12, 7, 2)
# grandiose_fight(example_player, example_boss)
# print(poutrage_index(example_player, example_boss))

boss_stats = ("🐹", 109, 8, 2)
player_stats = ("🎅", 100, 0, 0)

player_stuff = ((8, 0), (0, 2))

grandiose_fight(stuff_player(player_stats, player_stuff), Bonhomme(*boss_stats))
