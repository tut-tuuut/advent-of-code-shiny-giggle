from collections import defaultdict
import utils as u
import re
from PIL import Image, ImageDraw

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

parser_regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")


def parse_input(raw_input):
    return tuple(
        tuple(map(int, parser_regex.match(row).groups()))
        for row in raw_input.splitlines()
    )


def draw_lines(lines, case_width=1):
    max_x = max(max(line[0], line[2]) for line in lines)
    max_y = max(max(line[1], line[3]) for line in lines)
    img_file = Image.new(
        "RGB",
        (case_width * (1 + max_x), case_width * (1 + max_y)),
        (250, 250, 250),
    )
    drawing = ImageDraw.Draw(img_file)
    for line in lines:
        x1, y1, x2, y2 = line
        drawing.line(
            ((x1 * case_width, y1 * case_width), (x2 * case_width, y2 * case_width)),
            fill=(0, 0, 0, 100),
        )
    img_file.show()


def is_horizontal_or_vertical(line):
    x1, y1, x2, y2 = line
    return x1 == x2 or y1 == y2


def points_on_line(line):
    x1, y1, x2, y2 = line
    if x1 == x2:
        return ((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
    elif y1 == y2:
        return ((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))


def part_1(raw_input):
    lines = parse_input(raw_input)
    interesting_lines = tuple(filter(is_horizontal_or_vertical, lines))
    # draw_lines(interesting_lines,10)
    count_on_points = defaultdict(lambda: 0)
    for line in interesting_lines:
        for point in points_on_line(line):
            count_on_points[point] += 1
    counts = dict(count_on_points)
    return sum(1 if val > 1 else 0 for val in counts.values())
    # return len(set(point for point in set(every_point) if every_point.count(point) > 1))


u.assert_equals(part_1(example_input), 5)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
