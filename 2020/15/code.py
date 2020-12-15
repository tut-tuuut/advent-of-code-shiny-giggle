from collections import defaultdict

import utils as u

my_input = (1, 12, 0, 20, 8, 16)

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

examples = {
    (0, 3, 6): 436,
    (1, 3, 2): 1,
    (2, 1, 3): 10,
    (1, 2, 3): 27,
    (2, 3, 1): 78,
    (3, 2, 1): 438,
    (3, 1, 2): 1836,
}


def find_nth_number_in_drinking_game(starting_numbers, n):
    memorization = defaultdict(lambda: [])
    memorization.update(
        {number: [rank] for rank, number in enumerate(starting_numbers, 1)}
    )
    last_spoken_number = starting_numbers[-1]
    print(dict(memorization))
    for rank in range(len(starting_numbers) + 1, n + 1):
        print("------")
        print("rank", rank)
        print(dict(memorization))
        if len(memorization[last_spoken_number]) >= 2:
            print(
                f"{last_spoken_number} was seen at range {memorization[last_spoken_number][-2]}"
            )
            last_spoken_number = rank - 1 - memorization[last_spoken_number][-2]
        else:
            print(f"{last_spoken_number} is new")
            last_spoken_number = 0
        print("say", last_spoken_number)
        if rank == n:
            return last_spoken_number
        memorization[last_spoken_number].append(rank)


u.assert_equals(find_nth_number_in_drinking_game((0, 3, 6), 10), 0)

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
