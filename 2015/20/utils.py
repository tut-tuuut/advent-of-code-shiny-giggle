def assert_equals(tested, expected, comment=""):
    if tested == expected:
        print(f"\033[92m(YAY)\033[0m {tested} {comment}")
    else:
        print(f"\033[91m(NAY)\033[0m got {tested}, expected {expected}! {comment}")


def answer_part_1(content):
    print(f"\033[93m[PART 1] {content}\033[0m")


def answer_part_2(content):
    print(f"\033[93m[PART 2] {content}\033[0m")


PRIME_NUMBERS = (
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    179,
    103,
    181,
    107,
    191,
    109,
    193,
    113,
    197,
    127,
    199,
    131,
    211,
    137,
    223,
    139,
    227,
    149,
    229,
    151,
    233,
    157,
    239,
    163,
    241,
    167,
    251,
    173,
    257,
    263,
    269,
    271,
    277,
    281,
)