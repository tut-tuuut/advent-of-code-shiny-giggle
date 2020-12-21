RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
NORMAL = "\033[0m"
PURPLE = "\033[0;35m"


def red(message):
    print(f"{RED}{message}{NORMAL}")


def green(message):
    print(f"{GREEN}{message}{NORMAL}")


def yellow(message):
    print(f"{YELLOW}{message}{NORMAL}")


def purple(message):
    print(f"{PURPLE}{message}{NORMAL}")


def assert_equals(tested, expected, comment=""):
    if tested == expected:
        print(f"{GREEN}(YAY){NORMAL} {tested} {comment}")
    else:
        print(f"{RED}(NAY){NORMAL} got {tested}, expected {expected}! {comment}")


def answer_part_1(content):
    print(f"{YELLOW}[PART 1 🎄] {content}{NORMAL}")


def answer_part_2(content):
    print(f"{YELLOW}[PART 2 🌟] {content}{NORMAL}")
