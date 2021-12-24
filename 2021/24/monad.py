def monad(*args):
    inputs = list(args)
    w, x, y, z = 0, 0, 0, 0
    w = inputs.pop(0)
    x = 1
    y = w + 14
    z = y

    w = inputs.pop(0)
    x = z % 26
    x += 13
    x = int(x != w)

    y = 25
    y *= x
    y += 1
    z *= y

    y = (w + 8) * x
    z += y

    w = inputs.pop(0)
    x = (z % 26) + 11

    x = int(x != w)

    y = 25 * x + 1
    z *= y

    y = (w + 4) * x
    z += y

    w = inputs.pop(0)
    x = z

    x = (x % 26) + 10

    x = int(x != w)

    y = 25 * x + 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -3
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -4
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    x += 12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -8
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -3
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 1
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 1)
    x += 14
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 0
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -6
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 9
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 1)
    x += 11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = inputs.pop(0)
    x *= 0
    x += z
    x = x % 26
    z = int(z / 26)
    x += -12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 12
    y *= x
    z += y
    return w, x, y, z


print(monad(9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7))
