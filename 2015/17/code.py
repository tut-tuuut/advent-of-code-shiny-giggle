import utils as u


def find_all_possibilities(containers, target, possibilities=False):
    should_return_value = False
    if not possibilities:
        possibilities = set()
        should_return_value = True
    if sum(containers) < target:
        return 0
    if sum(containers) == target:
        possibilities.append(containers)
        return 1
    if sum(containers) > target:
        (
            find_all_possibilities(
                containers[:i] + containers[i + 1 :],
                target,
                possibilities=possibilities,
            )
            for i in range(len(containers))
        )
    if should_return_value:
        return len(possibilities)


exampleContainers = (20, 15, 10, 5, 5)

u.assert_equals(find_all_possibilities(exampleContainers, 25), 4)
