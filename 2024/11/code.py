import utils as u
import functools

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example = "0 1 10 99 999"


def blink(integers):
    result = []
    for integer in integers:
        if integer == 0:
            result.append(1)
        elif len(str(integer)) % 2 == 0:
            s = str(integer)
            h = int(len(s) / 2)
            result.append(int(s[:h]))
            result.append(int(s[h:]))
        else:
            result.append(2024 * integer)
    return result


def part_1(raw_str, times=25):
    integers = [int(s) for s in raw_str.split()]
    for _ in range(times):
        integers = blink(integers)
    return integers


u.assert_equal(part_1(example, 1), [1, 2024, 1, 0, 9, 9, 2021976])
u.assert_equal(
    part_1("125 17", 6),
    [
        int(x)
        for x in "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2".split()
    ],
)

u.answer_part_1(len(part_1(raw_input)))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# u.answer_part_1(len(part_1(raw_input, 75))) # TOO SLOW YO

# Let's count stones and cache results,
# instead of calculating their values and keeping them ALL in memory


@functools.cache
def blink_count(integer, times):
    if times == 0:
        return 1

    if integer == 0:
        return blink_count(1, times - 1)
    elif len(str(integer)) % 2 == 0:
        s = str(integer)
        h = int(len(s) / 2)
        return blink_count(int(s[:h]), times - 1) + blink_count(int(s[h:]), times - 1)
    else:
        return blink_count(2024 * integer, times - 1)


u.assert_equal(blink_count(125, 2), 2)


def part_2(raw_str, times=25):
    integers = [int(s) for s in raw_str.split()]
    return sum(blink_count(x, times) for x in integers)


u.assert_equal(part_2(raw_input), 187738)

u.answer_part_2(part_2(raw_input, 75))
