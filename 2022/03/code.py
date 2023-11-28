import utils

#with open(__file__ + ".input.txt", "r+") as file:
#    raw_input = file.read()

example_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

def find_item_in_both_compartments(rucksack_string):
    if len(rucksack_string)%2 != 0:
        raise Exception("I need an even-length string")
    compartment_size = int(len(rucksack_string)/2)
    first_compartment = set(rucksack_string[:compartment_size])
    second_compartment = set(rucksack_string[compartment_size:])
    return (first_compartment & second_compartment).pop()

utils.assert_equals(find_item_in_both_compartments("abcdaf"),"a")

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
