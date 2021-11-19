import hashlib
import time

input = "iwrupvqb"


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def find_lowest_match(prefix):
    i = 0
    while True:
        i += 1
        if md5(f"{prefix}{i}").startswith("0" * 5):
            return i


print(find_lowest_match(input))


def find_six_zeroes(prefix):
    i = 0
    while True:
        i += 1
        if i % 1000000 == 0:
            print(f"{time.ctime()} i = {i}")
        if md5(f"{prefix}{i}").startswith("0" * 6):
            return i


print(find_six_zeroes(input))
