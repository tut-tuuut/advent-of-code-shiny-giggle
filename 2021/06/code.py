from ast import parse
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = "3,4,3,1,2"

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def parse_input(raw_input):
    counters = tuple(int(x) for x in raw_input.split(","))
    return {value: counters.count(value) for value in range(9)}


def next_state(state):
    new_state = {value - 1: count for value, count in state.items()}
    new_fishes = new_state.pop(-1, 0)
    new_state[6] += new_fishes
    new_state[8] = new_fishes
    return new_state


def how_many_fishes_after_x_days(raw_input, nb_of_days):
    state = parse_input(raw_input)
    for _ in range(nb_of_days):
        state = next_state(state)
    return sum(state.values())


u.assert_equals(how_many_fishes_after_x_days(example_input, 80), 5934)
u.answer_part_1(how_many_fishes_after_x_days(raw_input, 80))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

u.assert_equals(how_many_fishes_after_x_days(example_input, 256), 26984457539)
u.answer_part_1(how_many_fishes_after_x_days(raw_input, 256))
