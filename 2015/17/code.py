import itertools
import utils as u


def find_all_possibilities(containers, target):
    if sum(containers) == target:
        return 1
    result = 0
    for i in range(len(containers) - 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == target:
                result += 1
    return result


exampleContainers = (20, 15, 10, 5, 5)


inputContainers = (
    33,
    14,
    18,
    20,
    45,
    35,
    16,
    35,
    1,
    13,
    18,
    13,
    50,
    44,
    48,
    6,
    24,
    41,
    30,
    42,
)


u.assert_equals(find_all_possibilities(exampleContainers, 25), 4)
u.assert_equals(find_all_possibilities(inputContainers, 150), 1304)

u.answer_part_1(find_all_possibilities(inputContainers, 150))
