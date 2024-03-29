def how_many_visited_houses(instructions):
    visited = {"0:0": True}
    x = 0
    y = 0
    #             ^y
    #             |
    #             |
    #     --------+---------->x
    #
    #
    for step in instructions:
        if step == ">":
            x += 1
        elif step == "<":
            x -= 1
        elif step == "v":
            y -= 1
        elif step == "^":
            y += 1
        else:
            next
        visited[key(x, y)] = True
    return len(visited)


def key(x, y):
    return f"{x}:{y}"


print(f"this should be 2: {how_many_visited_houses('>')}")
print(f"this should be 4: {how_many_visited_houses('^>v<')}")
print(f"this should be 2: {how_many_visited_houses('^v^v^v^v^v')}")
print(f"this should be 2: {how_many_visited_houses('^v^v^v^vs^v')}")

with open(__file__ + ".input.txt", "r+") as file:
    input = file.read()

print(
    f"with the drunken elf, santa will visit {how_many_visited_houses(input)} houses!"
)


def with_robosanta(instructions):
    visited = {"0:0": True}
    x, y, nx, ny = 0, 0, 0, 0
    for step in instructions:
        if step == ">":
            x += 1
        elif step == "<":
            x -= 1
        elif step == "v":
            y -= 1
        elif step == "^":
            y += 1
        else:
            next
        visited[key(x, y)] = True
        x, y, nx, ny = nx, ny, x, y  # !
    return len(visited)


print(f"this should be 3: {with_robosanta('^v')}")
print(f"this should be 3: {with_robosanta('^>v<')}")
print(f"this should be 11: {with_robosanta('^v^v^v^v^v')}")

print(f"With robosanta, santa will visit {with_robosanta(input)} houses!")
