import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()
INIT = 20151125
MULT = 252533
MODU = 33554393


def grid(row, column):
    diagonal_index = row + column - 1  # row where the diagonal begins
    initial_power = sum(range(diagonal_index))
    final_power = initial_power + column - 1
    result = INIT
    # apparently my computer did not like computing 20151125 * 252533 ** 17850353
    # so I did a dumb loop with intermediary modulos on each step.
    for _ in range(final_power):
        result = result * MULT % MODU
    return result


u.assert_equals(grid(2, 2), 21629792)
u.assert_equals(grid(3, 3), 1601130)
u.assert_equals(grid(1, 4), 30943339)
u.assert_equals(grid(1, 5), 10071777)
u.assert_equals(grid(5, 1), 77061)

u.answer_part_1(grid(2947, 3029))
