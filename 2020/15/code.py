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
    for rank in range(len(starting_numbers) + 1, n + 1):
        if rank % 1000 == 0:
            print(rank, end="\r")
        if len(memorization[last_spoken_number]) >= 2:
            last_spoken_number = rank - 1 - memorization[last_spoken_number][-2]
        else:
            last_spoken_number = 0
        if rank == n:
            return last_spoken_number
        # maybe for memory optimization we could shorten the list here,
        # to keep only the 2 last indexes. But it worked for both parts
        # without the optimization, so…
        memorization[last_spoken_number].append(rank)


u.assert_equals(find_nth_number_in_drinking_game((0, 3, 6), 10), 0)

for starting_numbers, expected in examples.items():
    u.assert_equals(find_nth_number_in_drinking_game(starting_numbers, 2020), expected)

u.answer_part_1(find_nth_number_in_drinking_game(my_input, 2020))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.answer_part_2(find_nth_number_in_drinking_game(my_input, 30000000))
