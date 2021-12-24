import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def alu_to_python_converter(name, raw_alu_innput):
    python = [f"def {name}(*args):"]
    S = "    "
    python.append(f"{S}inputs = list(args)")
    python.append(f"{S}w, x, y, z = 0, 0, 0, 0")
    for alu_row in raw_alu_innput.splitlines():
        alu_parts = alu_row.split(" ")
        instruction = alu_parts[0]
        arg1 = alu_parts[1]
        if len(alu_parts) == 3:
            arg2 = alu_parts[2]
        else:
            arg2 = ""

        if instruction == "inp":
            python.append(f"{S}{arg1} = inputs.pop(0)")
        elif instruction == "add":
            python.append(f"{S}{arg1} += {arg2}")
        elif instruction == "mul":
            python.append(f"{S}{arg1} *= {arg2}")
        elif instruction == "div":
            python.append(f"{S}{arg1} = int({arg1} / {arg2})")
        elif instruction == "mod":
            python.append(f"{S}{arg1} = {arg1} % {arg2}")
        elif instruction == "eql":
            python.append(f"{S}{arg1} = int({arg1} == {arg2})")
    python.append(f"{S}return w, x, y, z")
    return "\n".join(python)


example_1 = """inp x
mul x -1"""

example_2 = """inp z
inp x
mul z 3
eql z x"""

example_3 = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""

print(alu_to_python_converter("example_1", example_1))
print(alu_to_python_converter("example_2", example_2))
print(alu_to_python_converter("example_3", example_3))


def example_1(*args):
    inputs = list(args)
    w, x, y, z = 0, 0, 0, 0
    x = inputs.pop(0)
    x *= -1
    return w, x, y, z


def example_2(*args):
    inputs = list(args)
    w, x, y, z = 0, 0, 0, 0
    z = inputs.pop(0)
    x = inputs.pop(0)
    z *= 3
    z = int(z == x)
    return w, x, y, z


def example_3(*args):
    inputs = list(args)
    w, x, y, z = 0, 0, 0, 0
    w = inputs.pop(0)
    z += w
    z = z % 2
    w = int(w / 2)
    y += w
    y = y % 2
    w = int(w / 2)
    x += w
    x = x % 2
    w = int(w / 2)
    w = w % 2
    return w, x, y, z


print(example_2(3, 1))
print(example_3(14))


f = open("monad.py", "w")
f.write(alu_to_python_converter("monad", raw_input))
f.close()
