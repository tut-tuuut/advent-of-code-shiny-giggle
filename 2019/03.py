def manhattan_distance(a, b):
    xa, ya = a
    xb, yb = b
    return abs(xa - xb) + abs(ya - yb)


# print(f'this should be 6: {manhattan_distance([2,3], [-1,0])}')


def segment_intersection(ab, cd):
    if is_vertical(ab) and is_vertical(cd):
        return None
    if is_horizontal(ab) and is_horizontal(cd):
        return None
    xa, ya, xb, yb = ab
    xc, yc, xd, yd = cd
    if is_horizontal(ab):
        if min(xa, xb) < xc < max(xa, xb) and min(yd, yc) < ya < max(yd, yc):
            # print(f'17 - intersection btw {ab} and {cd} in {(xc, ya)}')
            return (xc, ya)
    elif is_vertical(ab):
        if min(ya, yb) < yc < max(ya, yb) and min(xc, xd) < xa < max(xc, xd):
            # print(f'21 - intersection btw {ab} and {cd} in {(xa,yc)}')
            return (xa, yc)


def is_vertical(ab):
    xa, ya, xb, yb = ab
    if xa == xb and ya != yb:
        return True
    return False


def is_horizontal(ab):
    xa, ya, xb, yb = ab
    if xa != xb and ya == yb:
        return True
    return False


# print(is_vertical((0,0,1,0)))
# print(is_vertical((0,0,0,7)))
# print(is_horizontal((0,0,1,0)))
# print(is_horizontal((0,0,0,7)))

# print(segment_intersection((-3, 0, 4, 0), (0, 4, 0, 1)))
# print(segment_intersection((-1, -3, -1, 4), (-2,-1,1,-1)))


def get_points_from_instructions(strInstructions):
    instructions = strInstructions.split(",")
    currentPosition = [0, 0]
    points = [(0, 0)]
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == "U":
            currentPosition[1] += steps
        elif direction == "D":
            currentPosition[1] -= steps
        elif direction == "R":
            currentPosition[0] += steps
        elif direction == "L":
            currentPosition[0] -= steps
        points.append(tuple(currentPosition))
    return points


def find_intersections_between_wires(firstWire, secondWire):
    intersections = []
    for i in range(len(firstWire) - 1):
        ab = firstWire[i] + firstWire[i + 1]
        for j in range(len(secondWire) - 1):
            cd = secondWire[j] + secondWire[j + 1]
            intersection = segment_intersection(ab, cd)
            if intersection != None:
                intersections.append(tuple(intersection))
    return intersections


# secondWire = get_points_from_instructions('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
# firstWire = get_points_from_instructions('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
# print(find_intersections_between_wires(firstWire, secondWire))
# print(min(list(map(lambda seg: manhattan_distance((0,0), seg), find_intersections_between_wires(firstWire, secondWire)))))

with open(__file__ + ".input") as file:
    input = list(map(get_points_from_instructions, file.read().split("\n")))

intersections_between_wires = find_intersections_between_wires(input[0], input[1])

print("Answer to part #1:")
print(
    min(
        list(
            map(
                lambda seg: manhattan_distance((0, 0), seg), intersections_between_wires
            )
        )
    )
)


def is_point_on_segment(point, segment):
    x, y = point
    xa, ya, xb, yb = segment
    if min(xa, xb) <= x <= max(xa, xb) and min(ya, yb) <= y <= max(ya, yb):
        return True
    return False


def segments(wire):
    for i in range(len(wire) - 1):
        yield wire[i] + wire[i + 1]


def wire_length_to_point(point, wire):
    length = 0
    for segment in segments(wire):
        xa, ya, xb, yb = segment
        if is_point_on_segment(point, segment):
            length += manhattan_distance((xa, ya), point)
            return length
        else:
            length += manhattan_distance((xa, ya), (xb, yb))


def find_most_efficient_intersection(wire1, wire2):
    intersections = find_intersections_between_wires(wire1, wire2)
    lengths = {}
    for i in intersections:
        lengths[i] = (wire_length_to_point(i, wire1), wire_length_to_point(i, wire2))
    print(min(list(map(sum, list(lengths.values())))))


find_most_efficient_intersection(input[0], input[1])
