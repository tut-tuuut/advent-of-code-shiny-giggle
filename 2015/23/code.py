import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# Part 1

example_program = """inc a
jio a, +2
tpl a
inc a"""


def exec_program(program: str, starting_a=0):
    registries = {"a": starting_a, "b": 0}
    pointer = 0
    rows = program.splitlines()
    try:
        while True:
            row = rows[pointer]
            instruction = row[:3]
            if instruction == "hlf":  # hlf a
                target = row[4]
                registries[target] //= 2
                pointer += 1
            elif instruction == "tpl":
                target = row[4]
                registries[target] *= 3
                pointer += 1
            elif instruction == "inc":
                target = row[4]
                registries[target] += 1
                pointer += 1
            elif instruction == "jmp":
                offset = int(row[4:])
                pointer += offset
            elif instruction == "jie":
                target = row[4]
                if registries[target] % 2 == 0:
                    offset = int(row[6:])
                    pointer += offset
                else:
                    pointer += 1
            elif instruction == "jio":
                target = row[4]
                if registries[target] == 1:
                    offset = int(row[6:])
                    pointer += offset
                else:
                    pointer += 1
    except IndexError:
        return registries


example = exec_program(example_program)

u.assert_equals(example["a"], 2)

result = exec_program(raw_input)
u.assert_equals(result["b"], 170)
u.answer_part_1(result["b"])

result = exec_program(raw_input, starting_a=1)
u.answer_part_2(result["b"])
