import utils as u
from itertools import product, count

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def next_step(vx, vy, x, y):
    x += vx
    y += vy
    vy -= 1
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    return vx, vy, x, y


def get_max_y(tx, txx, ty, tyy, vx0, vy0):
    vx = vx0
    vy = vy0
    x = 0
    y = 0
    target_acquired = False
    target_missed = False
    max_y = 0
    max_x = 0
    while target_acquired == False and target_missed == False:
        vx, vy, x, y = next_step(vx, vy, x, y)
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x
        if tx <= x <= txx and ty <= y <= tyy:
            target_acquired = True
        if txx < x or y < ty:
            target_missed = True
    if target_missed:
        return max_x, False
    if target_acquired:
        return max_x, max_y


def part_1(tx, txx, ty, tyy):
    max_vx = txx
    min_vx = 1
    min_vy = tyy
    max_vy = 450
    max_reached_y = 0
    max_reached_x = 0
    for i, v in enumerate(product(range(min_vx, max_vx), range(min_vy, max_vy))):
        vx, vy = v
        print(f"launching probe {i}", end="\r")
        _, reached_y = get_max_y(tx, txx, ty, tyy, vx, vy)
        if reached_y:
            if max_reached_y < reached_y:
                max_reached_y = reached_y
    print("")
    return max_reached_y


# u.assert_equals(get_max_y(20, 30, -10, -5, 6, 9), 45)
# u.assert_equals(part_1(20, 30, -10, -5), 45)
# u.answer_part_1(part_1(85,145,-163,-108))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def target_acquired(tx, txx, ty, tyy, vx0, vy0):
    vx = vx0
    vy = vy0
    x = 0
    y = 0
    target_acquired = False
    target_missed = False
    max_y = 0
    max_x = 0
    while target_acquired == False and target_missed == False:
        vx, vy, x, y = next_step(vx, vy, x, y)
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x
        if tx <= x <= txx and ty <= y <= tyy:
            target_acquired = True
        if txx < x or y < ty:
            target_missed = True
    return target_acquired, max_x, max_y


def part_2(tx, txx, ty, tyy):
    max_vx = txx + 5
    min_vx = 1
    min_vy = ty - 5
    max_vy = 300
    good_probes = 0
    for vx in range(min_vx, max_vx):  #
        for vy in range(min_vy, max_vy):
            ok, _, _ = target_acquired(tx, txx, ty, tyy, vx, vy)
            if ok:
                good_probes += 1
    return good_probes


u.assert_equals(part_2(20, 30, -10, -5), 112)

u.answer_part_2(part_2(85, 145, -163, -108))  # 5420 too low
