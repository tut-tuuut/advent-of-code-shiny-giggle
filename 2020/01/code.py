import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    input_string = file.read()


numbers = set(int(row) for row in input_string.split("\n") if row)

# part 1 -----------------------------------------------------
def find_numbers_which_sum_to_target(numbers, target):
    for number in numbers:
        if 2020 - number in numbers:
            return number * (target - number)


u.answer_part_1(find_numbers_which_sum_to_target(numbers, 2020))

# part 2 -----------------------------------------------------
def find_three_numbers_which_sum_to_target(numbers, target):
    for first_number in numbers:
        for second_number in numbers:
            if 2020 - first_number - second_number in numbers:
                return (
                    first_number * second_number * (2020 - first_number - second_number)
                )


u.answer_part_2(find_three_numbers_which_sum_to_target(numbers, 2020))
