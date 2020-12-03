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