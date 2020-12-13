import utils as u

raw_input = """Hit Points: 109
Damage: 8
Armor: 2"""

YELLOW = "\033[93m"
RED = "\033[91m"
NORMAL = "\033[0m"
GREEN = "\033[92m"

DISPLAY_WIDTH = 50


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
    """Generic character class. Could have named it "Character" but this is a French RPG."""

    def __init__(self, avatar, hp, attack, armor):
        self.avatar = avatar
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.armor = armor

    def take_a_gnon(self, attack):
        """Used when the bonhomme is hit by another bonhomme:
        GNON is a very technical French term designing a punch, a slap, etc.
        (derived from the word "onion", apparently)
        """
        self.hp -= attack - self.armor

    def display_status(self):
        draw_progress_bar(self.hp, self.max_hp, self.avatar)


# draw_progress_bar(60, 100, "😻")
# draw_progress_bar(10, 80, "🧚‍")
# draw_progress_bar(45, 120, "🐉")

boss = Bonhomme("🐉", 109, 8, 2)

boss.take_a_gnon(12)
boss.take_a_gnon(5)

boss.display_status()