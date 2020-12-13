def assert_equals(tested, expected, comment=""):
    if tested == expected:
        print(f"\033[92m(YAY)\033[0m {tested} {comment}")
    else:
        print(f"\033[91m(NAY)\033[0m got {tested}, expected {expected}! {comment}")


def answer_part_1(content):
    print(f"\033[93m[PART 1 🎄] {content}\033[0m")


def answer_part_2(content):
    print(f"\033[93m[PART 2 🌟] {content}\033[0m")
