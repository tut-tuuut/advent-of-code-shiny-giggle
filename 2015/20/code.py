import math
import time

import numpy
import scipy.stats as stats

import utils as u

# Easy part : calculate number of gifts from house number

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def get_number_of_gifts(house_number):
    result = 0
    return 10 * sigma(house_number)


# store a little bunch of sigmas: for every prime number under 100
# sigma(x) = x + 1 (a prime number only divides itself and 1)
sigmas = {prime: prime + 1 for prime in u.PRIME_NUMBERS}


def sigma(number):
    """sum of divisors of number"""
    # smartness #1: if we know it already, return it
    if number in sigmas:
        # print(f"smartness # we know already sigma({number})")
        return sigmas[number]

    # preparation for smartness #3: prime numbers are nice for sigma
    is_probably_prime = True

    # smartness #2: sigma is a multiplicative function:
    # if math.gcd(x,y) == 1 then sigma(x * y) = sigma(x) * sigma(y)
    # so we try to use memoization to avoid a huge loop when possible
    for x in range(2, number // 2):
        # if x does not divide number, continue:
        if number % x != 0:
            continue

        # if we are here, we found a divider to number, it's not a prime
        is_probably_prime = False

        y = number // x
        # if we cannot use the multiplicativeness of sigma, continue:
        if math.gcd(x, y) > 1:
            continue
        # if we are here, great!
        # print(f"hey! sigma({number}) = sigma({x})sigma({y})")
        sigmas[number] = sigma(x) * sigma(y)
        return sigmas[number]

    # smartness 3: if we did not find any divider to number,
    # calculate sigma as if it was a prime number. It is very difficult,
    # as you can see:
    if is_probably_prime:
        sigmas[number] = number + 1
        return sigmas[number]

    # no smartness worked, just sum all the dividers already
    sigmas[number] = sum(
        divisor for divisor in range(1, number + 1) if number % divisor == 0
    )
    return sigmas[number]


u.assert_equals(get_number_of_gifts(1), 10)
u.assert_equals(get_number_of_gifts(2), 30)
u.assert_equals(get_number_of_gifts(3), 40)
u.assert_equals(get_number_of_gifts(4), 70)
u.assert_equals(get_number_of_gifts(5), 60)
u.assert_equals(get_number_of_gifts(6), 120)
u.assert_equals(get_number_of_gifts(7), 80)
u.assert_equals(get_number_of_gifts(8), 150)
u.assert_equals(get_number_of_gifts(9), 130)

TARGET = 36000000
top_gifts = 0
house_number = 0
init_time = time.time()

for i in range(2, 1000000):
    if i % 1000 == 0:
        print(f"------ {i} - {time.time() - init_time} -------")
    nb_of_gifts = get_number_of_gifts(i)
    if nb_of_gifts > top_gifts:
        top_gifts = nb_of_gifts
        house_number = i
        print(f"{nb_of_gifts} gifts in house {i}")
        if nb_of_gifts > TARGET:
            u.answer_part_1(i)
            break

# 36902400 gifts in house 831600
# [PART 1] 831600
# the code need to run for 883 seconds for that ><
