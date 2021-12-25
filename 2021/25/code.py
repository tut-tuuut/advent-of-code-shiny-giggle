from more_itertools import windowed
import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def debug_state(state):
    print(f'┌{"─"*len(state[0])}┐')
    for row in state:
        print(f'│{"".join(row)}│')
    print(f'└{"─"*len(state[0])}┘')


def get_next_step(current_step):
    changed = False
    after_east_moves = []
    for row in current_step:
        row_string = "".join(row)
        row_string = row_string.replace(">.", ".>")
        new_row = list(row_string)
        if row[-1] == ">" and row[0] == ".":
            new_row[0] = ">"
            new_row[-1] = "."
            changed = True
        after_east_moves.append(new_row)
    after_south_moves = [[] for _ in range(len(current_step))]
    for col in range(len(current_step[0])):
        col_string = "".join(row[col] for row in after_east_moves)
        col_string = col_string.replace("v.", ".v")
        column = list(col_string)
        if after_east_moves[-1][col] == "v" and after_east_moves[0][col] == ".":
            column[0] = "v"
            column[-1] = "."
            changed = True
        for row, element in enumerate(column):
            after_south_moves[row].append(element)
    if not changed:
        changed = current_step != after_south_moves
    return after_south_moves, changed


def part_1(raw_input):
    state = [list(row) for row in raw_input.splitlines()]
    changed = True
    done_steps = 0
    while changed:
        state, changed = get_next_step(state)
        done_steps += 1
    return done_steps


u.assert_equals(part_1(example), 58)
u.answer_part_1(part_1(raw_input))
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
