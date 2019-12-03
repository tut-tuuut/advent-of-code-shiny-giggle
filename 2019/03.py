def manhattan_distance(a, b):
    xa, ya = a
    xb, yb = b
    return abs(xa - xb) + abs(ya - yb)

print(f'this should be 6: {manhattan_distance([2,3], [-1,0])}')