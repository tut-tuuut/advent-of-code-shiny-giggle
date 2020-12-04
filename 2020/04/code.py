import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

REQUIRED_FIELDS = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
)


def is_this_a_valid_passport(passport):
    return all(f"{field}:" in passport for field in REQUIRED_FIELDS)


def count_valid_passports_in_batch(raw_batch):
    return sum(
        1 for passport in raw_batch.split("\n\n") if is_this_a_valid_passport(passport)
    )


example_batch = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

u.assert_equals(count_valid_passports_in_batch(example_batch), 2)

u.answer_part_1(count_valid_passports_in_batch(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# criteria which are easily regexable:
EASY_CRITERIA = tuple(
    map(
        lambda p: re.compile(p, re.M),
        (
            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            # do the elves really define their hair color using hexcodes??
            r"hcl:#[0-9a-f]{6}\s",
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\s",
            #                 THIS ---------------^
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            r"pid:\d{9}\s",
        ),
    )
)

# byr, iyr, eyr should be 4 digits
# (other criteria on number value are dealt with later)
YEARS_CRITERIA = re.compile(r"(byr|iyr|eyr):(\d{4})\s", re.M)

# hgt (Height) - a number followed by either cm or in:
HEIGHT_CRITERIA = re.compile(r"hgt:(\d+)(in|cm)", re.M)


def is_this_valid_data(passport):
    passport += " "
    if not all(criteria.search(passport) for criteria in EASY_CRITERIA):
        print("easy criteria did not work")
        return False

    # then we will have to check manually…

    # print("------")
    # check years values.
    for key, year in YEARS_CRITERIA.findall(passport):
        # print(f"{key}:{year}")
        year = int(year)
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if key == "byr":
            if year < 1920 or year > 2002:
                return False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        elif key == "iyr":
            if year < 2010 or year > 2020:
                return False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        elif key == "eyr":
            if year < 2020 or year > 2030:
                return False

    # Add a beautiful separator before checking height value and units...
    # It's the only thing which is left to check before we can return True!
    # ALMOST THERE! HERE YOU GO PASSPORT
    #   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-
    #  / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \
    # `-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'
    # (Art by Richard Kirk)
    height = HEIGHT_CRITERIA.search(passport)
    if not height:
        return False
    number, unit = height.groups()
    if unit == "cm":
        return 150 <= int(number) <= 193
    elif unit == "in":
        return 59 <= int(number) <= 76


for valid_passport in """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".split(
    "\n\n"
):
    u.assert_equals(is_this_valid_data(valid_passport), True)

for invalid_passport in """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".split(
    "\n\n"
):
    u.assert_equals(is_this_valid_data(invalid_passport), False)


u.answer_part_2(
    sum(
        1
        for row in filter(is_this_a_valid_passport, raw_input.split("\n\n"))
        if is_this_valid_data(row)
    )
)
# 185 too high
# 110 too high