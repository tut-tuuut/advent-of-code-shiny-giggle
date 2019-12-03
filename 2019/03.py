def manhattan_distance(a, b):
    xa, ya = a
    xb, yb = b
    return abs(xa - xb) + abs(ya - yb)

#print(f'this should be 6: {manhattan_distance([2,3], [-1,0])}')

def segment_intersection(ab, cd):
    if is_vertical(ab) and is_vertical(cd):
        return None
    if is_horizontal(ab) and is_horizontal(cd):
        return None
    xa, ya, xb, yb = ab
    xc, yc, xd, yd = cd
    if is_horizontal(ab):
        if min(xa,xb) < xc < max(xa,xb) and min(yd, yc) < xa < max(yd, yc):
            return (xc, ya)
    elif is_vertical(ab):
        if min(ya, yb) < yc < max (ya, yb) and min(xc, xd) < xa < max(xc, xd):
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

#print(is_vertical((0,0,1,0)))
#print(is_vertical((0,0,0,7)))
#print(is_horizontal((0,0,1,0)))
#print(is_horizontal((0,0,0,7)))

print(segment_intersection((-3, 0, 4, 0), (0, 4, 0, 1)))
print(segment_intersection((-1, -3, -1, 4), (-2,-1,1,-1)))

def get_points_from_instructions(strInstructions):
    instructions = strInstructions.split(',')
    currentPosition = [0,0]
    points = [(0,0)]
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == 'U':
            currentPosition[1] += steps
        elif direction == 'D':
            currentPosition[1] -= steps
        elif direction == 'R':
            currentPosition[0] += steps
        elif direction == 'L':
            currentPosition[0] -= steps
        points.append(tuple(currentPosition))
    return points

firstWire = get_points_from_instructions('R8,U5,L5,D3')
secondWire = get_points_from_instructions('U7,R6,D4,L4')