import utils as u

# Solution inspired by the subreddit:
# instead of calculating the number of gifts from the house number,
# loop on the elves and have them "deliver presents" and store the
# amount of presents in every house.

max_houses = 36000000
house_limit_per_elf = 50
target = 36000000

points = [0] * max_houses
max_points = 0
for elf in range(1, max_houses):
    for house in range(elf, elf * (house_limit_per_elf + 1), elf):
        # print(f"elf {elf} fills house {house}")
        if house < max_houses:
            points[house] += 11 * elf
    if points[elf] > max_points:
        # the house with the same number as the elf will not be filled more,
        # hence the check on points[elf]
        print(f"{points[elf]} in house {elf}")
        max_points = points[elf]
    if points[elf] >= target:
        print("")
        u.answer_part_2(elf)
        break
