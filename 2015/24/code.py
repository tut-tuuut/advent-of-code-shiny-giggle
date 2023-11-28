import itertools
import math
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()
    package_list = set(map(int, raw_input.splitlines()))

example_packages = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11}


def balancing_packages_into_three(packages: tuple):
    total_weight = sum(packages)
    if total_weight % 3 > 0:
        raise RuntimeError("Impossible to balance the load, christmas is doomed!")
    group_weight = total_weight // 3
    found_first_group_size = False
    first_group_candidates = []
    for first_group_size in range(1, len(packages)):
        for first_group in itertools.combinations(packages, first_group_size):
            if sum(first_group) == group_weight:
                found_first_group_size = True
                first_group_candidates.append(first_group)
        if found_first_group_size:
            break
    return min(map(math.prod, first_group_candidates))


u.assert_equals(balancing_packages_into_three(example_packages), 99)
u.answer_part_1(balancing_packages_into_three(package_list))


# part 2
def balancing_packages_into_four(packages: tuple):
    total_weight = sum(packages)
    if total_weight % 4 > 0:
        raise RuntimeError("Impossible to balance the load, christmas is doomed!")
    group_weight = total_weight // 4
    found_first_group_size = False
    first_group_candidates = []
    for first_group_size in range(1, len(packages)):
        for first_group in itertools.combinations(packages, first_group_size):
            if sum(first_group) == group_weight:
                found_first_group_size = True
                first_group_candidates.append(first_group)
        if found_first_group_size:
            break
    return min(map(math.prod, first_group_candidates))


u.assert_equals(balancing_packages_into_four(example_packages), 44)
u.answer_part_2(balancing_packages_into_four(package_list))
