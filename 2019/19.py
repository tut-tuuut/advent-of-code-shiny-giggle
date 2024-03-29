import intcode as ic
import itertools as it

program = (
    109,
    424,
    203,
    1,
    21101,
    11,
    0,
    0,
    1105,
    1,
    282,
    21101,
    0,
    18,
    0,
    1106,
    0,
    259,
    1202,
    1,
    1,
    221,
    203,
    1,
    21101,
    0,
    31,
    0,
    1105,
    1,
    282,
    21102,
    1,
    38,
    0,
    1106,
    0,
    259,
    20101,
    0,
    23,
    2,
    22102,
    1,
    1,
    3,
    21101,
    1,
    0,
    1,
    21101,
    0,
    57,
    0,
    1106,
    0,
    303,
    1202,
    1,
    1,
    222,
    21002,
    221,
    1,
    3,
    21001,
    221,
    0,
    2,
    21102,
    1,
    259,
    1,
    21101,
    80,
    0,
    0,
    1105,
    1,
    225,
    21102,
    1,
    117,
    2,
    21102,
    1,
    91,
    0,
    1105,
    1,
    303,
    1202,
    1,
    1,
    223,
    20102,
    1,
    222,
    4,
    21101,
    0,
    259,
    3,
    21101,
    0,
    225,
    2,
    21101,
    225,
    0,
    1,
    21101,
    118,
    0,
    0,
    1105,
    1,
    225,
    21001,
    222,
    0,
    3,
    21101,
    20,
    0,
    2,
    21102,
    1,
    133,
    0,
    1105,
    1,
    303,
    21202,
    1,
    -1,
    1,
    22001,
    223,
    1,
    1,
    21101,
    0,
    148,
    0,
    1106,
    0,
    259,
    2101,
    0,
    1,
    223,
    20102,
    1,
    221,
    4,
    21001,
    222,
    0,
    3,
    21101,
    0,
    16,
    2,
    1001,
    132,
    -2,
    224,
    1002,
    224,
    2,
    224,
    1001,
    224,
    3,
    224,
    1002,
    132,
    -1,
    132,
    1,
    224,
    132,
    224,
    21001,
    224,
    1,
    1,
    21102,
    195,
    1,
    0,
    105,
    1,
    108,
    20207,
    1,
    223,
    2,
    21002,
    23,
    1,
    1,
    21102,
    -1,
    1,
    3,
    21101,
    0,
    214,
    0,
    1105,
    1,
    303,
    22101,
    1,
    1,
    1,
    204,
    1,
    99,
    0,
    0,
    0,
    0,
    109,
    5,
    1201,
    -4,
    0,
    249,
    22102,
    1,
    -3,
    1,
    22101,
    0,
    -2,
    2,
    21202,
    -1,
    1,
    3,
    21102,
    1,
    250,
    0,
    1106,
    0,
    225,
    22102,
    1,
    1,
    -4,
    109,
    -5,
    2105,
    1,
    0,
    109,
    3,
    22107,
    0,
    -2,
    -1,
    21202,
    -1,
    2,
    -1,
    21201,
    -1,
    -1,
    -1,
    22202,
    -1,
    -2,
    -2,
    109,
    -3,
    2106,
    0,
    0,
    109,
    3,
    21207,
    -2,
    0,
    -1,
    1206,
    -1,
    294,
    104,
    0,
    99,
    21202,
    -2,
    1,
    -2,
    109,
    -3,
    2105,
    1,
    0,
    109,
    5,
    22207,
    -3,
    -4,
    -1,
    1206,
    -1,
    346,
    22201,
    -4,
    -3,
    -4,
    21202,
    -3,
    -1,
    -1,
    22201,
    -4,
    -1,
    2,
    21202,
    2,
    -1,
    -1,
    22201,
    -4,
    -1,
    1,
    21201,
    -2,
    0,
    3,
    21101,
    343,
    0,
    0,
    1105,
    1,
    303,
    1105,
    1,
    415,
    22207,
    -2,
    -3,
    -1,
    1206,
    -1,
    387,
    22201,
    -3,
    -2,
    -3,
    21202,
    -2,
    -1,
    -1,
    22201,
    -3,
    -1,
    3,
    21202,
    3,
    -1,
    -1,
    22201,
    -3,
    -1,
    2,
    21201,
    -4,
    0,
    1,
    21101,
    0,
    384,
    0,
    1105,
    1,
    303,
    1105,
    1,
    415,
    21202,
    -4,
    -1,
    -4,
    22201,
    -4,
    -3,
    -4,
    22202,
    -3,
    -2,
    -2,
    22202,
    -2,
    -4,
    -4,
    22202,
    -3,
    -2,
    -3,
    21202,
    -4,
    -1,
    -2,
    22201,
    -3,
    -2,
    1,
    22101,
    0,
    1,
    -4,
    109,
    -5,
    2105,
    1,
    0,
)


def is_tracted(x, y):
    computer = ic.Computer(list(program))
    for result in computer.run([x, y]):
        return result


def part1():
    grid = []
    count = 0
    for x, y in it.product(range(50), repeat=2):
        print(f"computing part 1... {100*x/50}%", end="\r")
        if is_tracted(x, y):
            count += 1
    print("computing part 1... DONE! 🤩\n\n")
    print(f"part 1 result: {count}")


# part1()


def part2():
    minx = 104
    maxx = 145
    y = 299
    while (maxx - minx) < 100:
        y += 1
        while is_tracted(minx, y) == 0:
            minx += 1  # find minimum and maximum x which yield 1
        while is_tracted(maxx, y) == 1:
            maxx += 1
        print(f"width of beam at y= {y}: {maxx - minx}", end="\r")
        # and if maxx - minxx >= 100 that could be good
    print("\n\n")
    x = minx - 1
    miny = y
    for x in range(minx, minx + 10):
        s = ""
        for y in range(miny, miny + 10):
            if is_tracted(x, y) == 1:
                s += "#"
            else:
                s += "."
        print(f"x = {x} : {s}")
    print("\n\n")


part2()
