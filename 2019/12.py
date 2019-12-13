import itertools as it

puzzleInput = """<x=1, y=-4, z=3>
<x=-14, y=9, z=-4>
<x=-4, y=-6, z=7>
<x=6, y=-9, z=-11>"""

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
            print(f'{moon.name}: {moon.x} {moon.y} {moon.z} | {moon.vx} {moon.vy} {moon.vz}')
    def apply_gravity(self):
        for m,n in it.combinations(self.moons, 2):
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
io = Moon('io', 1, -4, 3)
europa = Moon('europa', -14, 9, -4)
ganymede = Moon('ganymede', -4, -6, 7)
callisto = Moon('callisto', 6, -9, -11)

# example input
#io = Moon('io', -1, 0, 2)
#europa = Moon('europa',2, -10, -7)
#ganymede = Moon('ganymede', 4, -8, 8)
#callisto = Moon('callisto',3, 5, -1)

jupiter = System()
jupiter.add(io)
jupiter.add(europa)
jupiter.add(ganymede)
jupiter.add(callisto)

# calculons les niveaux d'énergie de chaque lune individuellement pour 4000 steps
numberOfSteps = 2000
energySets = []
for i in range(2*numberOfSteps):
    jupiter.step()
    energies = []
    for m in jupiter.moons:
        energies.append(m.kinetic_energy())
        energies.append(m.potential_energy())
    energySets.append(tuple(energies))

# lièvre + tortue pour trouver des périodicités dans les niveaux d'énergie individuels
periods = []
for i in range(1,numberOfSteps):
    rabbit = energySets[2*i]
    turtle = energySets[i]
    for index,energy in enumerate(turtle):
        if energy == rabbit[index]:
            print(f'for index {index} we may have a periodicity of {i}')

# et ensuite la périodicité globale et le plus petit multiple commun des périodicités individuelles