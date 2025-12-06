import utils as u
import numpy as np

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

u.answer_part_1("allez")


def part_1(given_input):
    given_input_as_tuple = tuple(given_input.splitlines())
    arr = np.array(
        tuple(
            tuple(int(cell) for cell in row.split())
            for row in given_input_as_tuple[:-1]
        )
    )
    print(arr)


part_1(example)
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
