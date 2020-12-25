RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
PINK = "\033[38;5;206m"

NORMAL = "\033[0m"


def red(message):
    print(f"{RED}{message}{NORMAL}")


def green(message):
    print(f"{GREEN}{message}{NORMAL}")


def yellow(message):
    print(f"{YELLOW}{message}{NORMAL}")


def purple(message):
    print(f"{PURPLE}{message}{NORMAL}")


def blue(message):
    print(f"{CYAN}{message}{NORMAL}")


def pink(message):
    print(f"{PINK}{message}{NORMAL}")


def assert_equals(tested, expected, comment=""):
    if tested == expected:
        print(f"{GREEN}(YAY){NORMAL} {tested} {comment}")
    else:
        print(f"{RED}(NAY){NORMAL} got {tested}, expected {expected}! {comment}")


def answer_part_1(content):
    print(f"{YELLOW}[PART 1 🎄] {content}{NORMAL}")


def answer_part_2(content):
    print(f"{YELLOW}[PART 2 🌟] {content}{NORMAL}")


if __name__ == "__main__":
    purple("violet !")
    blue("bleu !")
    green("vert !")
    yellow("jaune !")
    red("rouge !")
    pink("rose !")
    answer_part_1("réponse partie 1")
    answer_part_2("réponse partie 2")
    assert_equals("réel", "attendu", "test pour voir un test échouer")
    assert_equals("youpi", "youpi", "pour voir quand un test passe")
