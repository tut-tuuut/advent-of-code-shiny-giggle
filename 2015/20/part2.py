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

# target = 36M
# we are looking for x such as some numbers between x/50 and x/2
# sum up to 36M/11
# so x/50 + x/2 ~ 3,6M
# x ~ 7M
# for x = 7M it works, but I fear it's too high

# 1501920 is too high
# 803982


def get_number_of_gifts(house_number):
    return house_number + sum(
        11 * elf
        for elf in range(math.ceil(house_number / 50), math.ceil(house_number / 2))
        if house_number % elf == 0
    )


get_number_of_gifts(991)

# I tried using an increment of 410 to have numbers which
# N/2 and N/3 and N/7 and N/4 would be in the sum…
# It gave me answer 1330560 which is too high.

starting_point = 95970
increment = 6
max_gifts = 1377855

TARGET = 36000000
init_time = time.time()

# use 210 increment so we are targeting multiples of 2 and 3 and 5 and 7,
# so N/2 and N/3 and n/5 and n/7 will be in the sum
for i in range(starting_point, starting_point + 3200 * increment, increment):
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
