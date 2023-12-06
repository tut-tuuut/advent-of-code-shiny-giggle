import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

# done on excel


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

input_race_time, input_record = (int(row) for row in raw_input.split())
example_time, example_record = 71530, 940200


def distance(button_time, race_time):
    return int(button_time) * (race_time - int(button_time))


def find_first_winning_button_time(race_time, record):
    step = int(race_time / 2)
    value = int(race_time / 2)  # I know it's always the max
    tested_values = {}
    winning_values = set()
    # let's search par dichotomie
    while step >= 1:
        step = int(step / 2)
        d = distance(value, race_time)
        tested_values[value] = d
        print(value)
        if d > record:
            # it's winning, try to push for less long
            winning_values.add(value)
            value -= step
            # print(f"  -> winning: decrease value by {step}")
        elif d <= record:
            # we lose, try to push longer
            value += step
            # print(f"  -> losing: increase value by {step}")
    # when we reached step == 1, we are close but not to the good solution yet.
    # increase by unity steps until we find the balance point
    if d <= record:
        while d <= record:
            # we lose, try to poush 1ms longer
            d = distance(value, race_time)
            tested_values[value] = d
            if d > record:
                winning_values.add(value)
            value += 1
    elif d > record:
        while d > record:
            d = distance(value, race_time)
            if d > record:
                winning_values.add(value)
            value -= 1
    return min(winning_values)


u.assert_equal(find_first_winning_button_time(example_time, example_record), 14)


def part_2(race_time, record):
    first_winning_value = find_first_winning_button_time(race_time, record)
    second_winning_value = race_time - first_winning_value
    print(first_winning_value, second_winning_value)
    return second_winning_value - first_winning_value + 1
    # first_winning = 4 ; last winning = 7 ; race = 12 ; 4 winning ways (7 - 4 +1)
    # llllwwwwllll
    # 12 - 4 = 8

    # race = 13 ; first winning = 3 ; last winning = 9 ; 7 winning ways (9 - 3 + 1)
    # lllxxxMxxxlll
    # 13 - 3 = 10


u.assert_equal(part_2(example_time, example_record), 71503)
u.answer_part_2(part_2(input_race_time, input_record))

print(distance(4826341, input_race_time) - input_record)
print(distance(4826340, input_race_time) - input_record)
