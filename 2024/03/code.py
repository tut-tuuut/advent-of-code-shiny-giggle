import utils as u
import re

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def part1(raw_string):
    result = 0
    for m in re.finditer(regex, raw_string):
        result += int(m[1]) * int(m[2])
    return result


u.assert_equal(part1(example), 161)
u.answer_part_1(part1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part2(raw_str):
    returnvalue = 0
    remain = raw_str
    instruction, nextinstruction = "do()", "don't()"
    result = remain.split(nextinstruction, maxsplit=1)
    while len(result) == 2:
        todo_now, remain = result
        if nextinstruction == "don't()":
            returnvalue += part1(todo_now)
        instruction, nextinstruction = nextinstruction, instruction
        result = remain.split(nextinstruction, maxsplit=1)
    if instruction == "do()":
        returnvalue += part1(remain)
    return returnvalue


example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
u.assert_equal(part2(example2), 48)

u.answer_part_2(part2(raw_input))
