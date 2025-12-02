import utils as u
from collections import namedtuple
from PIL import Image

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

Robot = namedtuple("Robot", ("x", "y", "vx", "vy"))

example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def part_1(raw_str, width=101, height=103, seconds=100):
    robots = []
    for row in raw_str.splitlines():
        pstr, vstr = row[2:].split(" v=")
        x, y = (int(i) for i in pstr.split(","))
        vx, vy = (int(i) for i in vstr.split(","))
        x = (x + seconds * vx) % width
        y = (y + seconds * vy) % height
        robots.append(Robot(x, y, vx, vy))
    quad_nw = sum(
        1 for rob in robots if rob.x < (width - 1) / 2 and rob.y < (height - 1) / 2
    )
    quad_ne = sum(
        1 for rob in robots if rob.x < (width - 1) / 2 and rob.y > (height - 1) / 2
    )
    quad_sw = sum(
        1 for rob in robots if rob.x > (width - 1) / 2 and rob.y < (height - 1) / 2
    )
    quad_se = sum(
        1 for rob in robots if rob.x > (width - 1) / 2 and rob.y > (height - 1) / 2
    )

    return quad_ne * quad_nw * quad_sw * quad_se


u.assert_equal(part_1(example, width=11, height=7), 12)


u.answer_part_1(part_1(raw_input))
# 232364160 too high

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def draw(robots, name, width=101, height=103):
    img = Image.new("RGB", (width, height))
    for rob in robots:
        img.putpixel((rob.x, rob.y), (70, 255, 50))
    img.save(name)


def part_2(raw_str, width=101, height=103, start=100, end=200):
    for sec in range(start, end):
        robots = []
        for row in raw_str.splitlines():
            pstr, vstr = row[2:].split(" v=")
            x, y = (int(i) for i in pstr.split(","))
            vx, vy = (int(i) for i in vstr.split(","))
            x = (x + sec * vx) % width
            y = (y + sec * vy) % height
            robots.append(Robot(x, y, vx, vy))
        draw(robots, f"{sec}.png")


part_2(raw_input, start=3000, end=7000)
