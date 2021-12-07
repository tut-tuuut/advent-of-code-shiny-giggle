import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = "16,1,2,0,4,2,7,1,2,14"
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def fuel_consumed_for_position(target, positions):
    return sum(abs(target - x) for x in positions)


def where_should_we_align_the_crabs(raw_input):
    positions = tuple(map(int, raw_input.split(",")))
    min_consumed_fuel = 5 * sum(positions)
    optimal_position = None
    for x in range(min(positions), max(positions)):
        fuel = fuel_consumed_for_position(x, positions)
        if fuel < min_consumed_fuel:
            min_consumed_fuel = fuel
            optimal_position = x
    return optimal_position, min_consumed_fuel


u.assert_equals(where_should_we_align_the_crabs(example_input), (2, 37))
u.answer_part_1(where_should_we_align_the_crabs(raw_input)[1])

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def fuel_consumed_for_position_part2(target, positions):
    # maths: sum(1,2....,N) = N*(N+1)/2
    return sum(
        int(abs(target - crab) * (1 + abs(target - crab)) / 2) for crab in positions
    )


def where_should_we_align_the_crabs_part2(raw_input):
    positions = tuple(map(int, raw_input.split(",")))
    min_consumed_fuel = None
    optimal_position = None
    for x in range(min(positions), max(positions)):
        fuel = fuel_consumed_for_position_part2(x, positions)
        if min_consumed_fuel is None or fuel < min_consumed_fuel:
            min_consumed_fuel = fuel
            optimal_position = x
    return optimal_position, min_consumed_fuel


u.assert_equals(where_should_we_align_the_crabs_part2(example_input), (5, 168))
u.answer_part_2(where_should_we_align_the_crabs_part2(raw_input)[1])

# 2332855 too low
