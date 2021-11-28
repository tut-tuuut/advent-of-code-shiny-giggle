import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()


# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def count_constellations(raw_input):
    points = tuple(
        tuple(int(d) for d in row.split(",")) for row in raw_input.splitlines()
    )
    constellation_numbers = list(range(len(points)))
    for idx, point in enumerate(points):
        for i in range(idx + 1, len(constellation_numbers)):
            other_point = points[i]
            if d(other_point, point) <= 3:
                plops = (constellation_numbers[idx], constellation_numbers[i])
                new_constellation_number = min(plops)
                constellation_numbers = [
                    x if x not in plops else new_constellation_number
                    for x in constellation_numbers
                ]
    return len(set(constellation_numbers))


def d(a, b):
    return sum(abs(b[i] - a[i]) for i in range(len(a)))


u.assert_equals(d((0, 0, 0, 0), (3, 0, 0, 0)), 3)
u.assert_equals(d((0, 0, 0, 3), (0, 0, 0, 6)), 3)

example_1 = """0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0"""

example_2 = """-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""

example_3 = """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2"""

example_4 = """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""

u.assert_equals(count_constellations(example_1), 2)
u.assert_equals(count_constellations(example_2), 4)
u.assert_equals(count_constellations(example_3), 3)
u.assert_equals(count_constellations(example_4), 8)

u.answer_part_1(count_constellations(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
