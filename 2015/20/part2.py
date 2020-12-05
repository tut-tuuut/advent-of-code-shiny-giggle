import math
import time

import numpy
import scipy.stats as stats

import utils as u


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# elf 1 visits 50 houses:
# 1,2,3...49,50
# elf 2 visits 50 houses:
# 2,4,6....100
# elf 3 : 3,6,9...150
# elf 4 : 4,8,12..200 <-- !
# elf 5 : 5,10,...250
# elf 6 : 6,12....300
# elf 7 : 7,14....350
# ...
# elf 199: 199...9950
# elf 200: 200...10000 <-- !

# elf N visits houses between N and 50 * N

# in house number H:
# elf N may visit it if N < H < 50 * N

# if H = 200, elves will visit only if their nb is between 4 and 200:
# elf 4 will visit 4 to 200
# elf 200 will visit 200 to 10000
# so elves will v isit only if their nb is between H/50 and H


def get_number_of_gifts(house_number):
    return house_number + sum(
        11 * elf
        for elf in range(math.ceil(house_number / 50), math.ceil(house_number / 2))
        if house_number % elf == 0
    )


get_number_of_gifts(991)

starting_point = 838377
TARGET = 36000000
init_time = time.time()
max_gifts = 0

for i in range(starting_point, starting_point + 1000):
    gifts = get_number_of_gifts(i)
    print(
        f"------ house {i} - {gifts:08} gifts - time {time.time() - init_time} -------",
        end="\r",
    )
    if max_gifts < gifts:
        max_gifts = gifts
        print("")
    if gifts > TARGET:
        print("\n")
        u.answer_part_2(i)
        break
print(f"\ntime {time.time() - init_time}")
