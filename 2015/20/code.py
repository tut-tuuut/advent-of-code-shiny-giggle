import math

import numpy
import scipy.stats as stats

import utils as u

# Easy part : calculate number of gifts from house number
prime_numbers = [2, 3, 5, 7, 11]


def yield_prime_numbers_before(target):
    max_known_prime_number = max(prime_numbers)
    if target < max_known_prime_number:
        yield from (i for i in prime_numbers if i <= target)
    if target > max_known_prime_number:
        yield from prime_numbers
        for i in range(max_known_prime_number, target):
            prime = True
            for j in prime_numbers:
                if i % j == 0:
                    prime = False
                    break
            if prime == True:
                prime_numbers.append(i)
                yield i


def get_prime_divisors(number):
    for prime_divisor in yield_prime_numbers_before(number):
        divisor = prime_divisor
        while number % divisor == 0:
            yield prime_divisor
            divisor *= prime_divisor


def get_number_of_gifts(house_number):
    result = 0
    return 10 * sum(
        elf for elf in range(1, house_number + 1) if house_number % elf == 0
    )


print(list(get_prime_divisors(725)))

# it works but it's an O(n)


# house 10:
# elf 1, 2, 5, 10 come by, result = 10*(1 + 2 + 5 + 10) = 10 * 18

# house 9:
# elf 1, 3, 9 come by, result = 10*(1+3+9) = 10 * 13

# min value of gifts for house N  = 10 + N for houses which are prime numbers

# house 20:
# elf 1, 2, 4, 5, 10, 20 stop by
# prime factors 2,2,5 => elves 2 and 5
# not prime factors 4, 10 : combinations of prime factors 2*2 and 2*5

# house 100:
# elves 1, 2, 4, 5, 10, 20, 50
# prime factors 5 5 2 2
# snap, not a good example

# house 16
# elves 1, 2, 4, 8, 16
# prime factors 2 2 2 2
# combinations 2*2=4 2*2*2=8

# house 6
# elves 1, 2, 3, 6
# prime factors 2 3
# combinations others than 6: none

# house 8
# elves 1, 2, 4, 8
# prime factors 2 2 2
# combinations : 2*2

#
# so maybe we can make a get_number_of_gifts which is not a O(n) ?
# with a result which could be
#      10 * (1 + N)
#      + something with unique prime factors < N
#      + something with combinations of prime factors with product < N

# house 8:
# elf 1, 2, 4,

u.assert_equals(get_number_of_gifts(1), 10)
u.assert_equals(get_number_of_gifts(2), 30)
u.assert_equals(get_number_of_gifts(3), 40)
u.assert_equals(get_number_of_gifts(4), 70)
u.assert_equals(get_number_of_gifts(5), 60)
u.assert_equals(get_number_of_gifts(6), 120)
u.assert_equals(get_number_of_gifts(7), 80)
u.assert_equals(get_number_of_gifts(8), 150)
u.assert_equals(get_number_of_gifts(9), 130)
u.assert_equals(get_number_of_gifts(10), 180)

# Hard part : find the house which gets 36 million gifts.
target = 36000000

# When you look at the graph, you see that some houses
# are over privileged, and their gift count seems to follow a line:
# try to calculate the values of this line to search around where the line
# reaches 36M.
"""
max_gifts = 0
houses = []
gift_counts = []
print("calculating the over privileged houses...")
for house in range(1000, 10000):
    if house % 1000 == 0:
        print(".", end="")
    nb_gifts = get_number_of_gifts(house)
    if nb_gifts > max_gifts:
        if max_gifts > 0:
            houses.append(house)
            gift_counts.append(nb_gifts)
        max_gifts = nb_gifts
print(" done!")
x = numpy.array(houses)
y = numpy.array(gift_counts)
"""
# the line has the equation a * nb_house + b = nb_gift !
# so I could look at house number (36M - b) / a
"""
a, b, _, _, _ = stats.linregress(x, y)
starting_house = int((target - b) / a)
print(f"a = {a} b = {b}")
print("looking for the house with 36M gifts...")
"""
max_gifts = 0
for house in range(50000, 100000):
    if house % 1000 == 0:
        print("house", house)
    nb_gifts = get_number_of_gifts(house)
    if nb_gifts > max_gifts:
        max_gifts = nb_gifts
        print(f"house {house} : {nb_gifts} gifts")
        if nb_gifts >= target:
            u.answer_part_1(house)

# 971880 too high????? duh
# 970200 too high too… noes

# so I will start at 971879 and go down until I find another good one