import itertools as it
from math import gcd


def lcm(listOfInts):
    lcm = listOfInts[0]
    for i in listOfInts[1:]:
        lcm = int(lcm * i / gcd(lcm, i))
    return lcm


class Moon:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()


class System:
    def __init__(self):
        self.moons = []

    def add(self, moon):
        self.moons.append(moon)

    def debug(self):
        for moon in self.moons:
            print(
                f"{moon.name}: {moon.x} {moon.y} {moon.z} | {moon.vx} {moon.vy} {moon.vz}"
            )

    def x(self):
        data = []
        for moon in self.moons:
            data.append(str(moon.x))
            data.append(str(moon.vx))
        return ".".join(data)

    def y(self):
        data = []
        for moon in self.moons:
            data.append(str(moon.y))
            data.append(str(moon.vy))
        return ".".join(data)

    def z(self):
        data = []
        for moon in self.moons:
            data.append(str(moon.z))
            data.append(str(moon.vz))
        return ".".join(data)

    def apply_gravity(self):
        for m, n in it.combinations(self.moons, 2):
            if m.x > n.x:
                m.vx -= 1
                n.vx += 1
            elif m.x < n.x:
                m.vx += 1
                n.vx -= 1
            if m.y > n.y:
                m.vy -= 1
                n.vy += 1
            elif m.y < n.y:
                m.vy += 1
                n.vy -= 1
            if m.z > n.z:
                m.vz -= 1
                n.vz += 1
            elif m.z < n.z:
                m.vz += 1
                n.vz -= 1

    def apply_velocity(self):
        for m in self.moons:
            m.x += m.vx
            m.y += m.vy
            m.z += m.vz

    def step(self):
        self.apply_gravity()
        self.apply_velocity()

    def energy(self):
        return sum(list(map(lambda moon: moon.total_energy(), self.moons)))


# puzzle input
io = Moon("io", 1, -4, 3)
europa = Moon("europa", -14, 9, -4)
ganymede = Moon("ganymede", -4, -6, 7)
callisto = Moon("callisto", 6, -9, -11)

# example input
# io = Moon('io', -1, 0, 2)
# europa = Moon('europa',2, -10, -7)
# ganymede = Moon('ganymede', 4, -8, 8)
# callisto = Moon('callisto',3, 5, -1)

jupiter = System()
jupiter.add(io)
jupiter.add(europa)
jupiter.add(ganymede)
jupiter.add(callisto)

numberOfSteps = 3000
xdata = []
ydata = []
zdata = []
periods = {}
for i in it.count():
    print(f"Analyzing... step {i}", end="\r")
    if "x" not in periods.keys():
        x = jupiter.x()
        if x in xdata:
            periods["x"] = i
            print(f"{i} may be a period for x")
            del xdata
        else:
            xdata.append(x)

    if "y" not in periods.keys():
        y = jupiter.y()
        if y in ydata:
            periods["y"] = i
            print(f"{i} may be a period for y")
            del ydata
        else:
            ydata.append(y)

    if "z" not in periods.keys():
        z = jupiter.z()
        if z in zdata:
            periods["z"] = i
            print(f"{i} may be a period for z")
            del zdata
        else:
            zdata.append(z)

    if len(periods.keys()) == 3:
        print("Found 3 periods! I’m done!")
        break

    jupiter.step()

print(periods)
print(f"answer: {lcm(list(periods.values()))}")
