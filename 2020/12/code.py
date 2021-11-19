import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """F10
N3
F7
R90
F11"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
#
#       ~     y 90°  ~
#   ~         ^    ~
#       ~     |  ~    ~
# 180° -x <-- 0 --> x 0°
#        ~    |   ~
#    ~        v      ~
#     ~      -y  270°
#  ~     ~
#
def manhattan(x, y):
    return abs(x) + abs(y)


class Ferry:
    DIRECTIONS = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}

    def __init__(self):
        self.position = [0, 0]  # x y
        self.orientation = 0  # in degrees, trigonometric-oriented

    def executeInstruction(self, raw_instruction):
        instruction = raw_instruction[0]
        argument = int(raw_instruction[1:])
        if instruction == "N":
            self.moveInDirection(self.DIRECTIONS[90], argument)
        elif instruction == "S":
            self.moveInDirection(self.DIRECTIONS[270], argument)
        elif instruction == "E":
            self.moveInDirection(self.DIRECTIONS[0], argument)
        elif instruction == "W":
            self.moveInDirection(self.DIRECTIONS[180], argument)
        elif instruction == "F":
            self.moveInDirection(self.DIRECTIONS[self.orientation], argument)
        elif instruction == "R":
            self.orientation = (self.orientation - argument) % 360
        elif instruction == "L":
            self.orientation = (self.orientation + argument) % 360

    def moveInDirection(self, direction, distance):
        self.position[0] += direction[0] * distance
        self.position[1] += direction[1] * distance

    def followNavigationInstructions(self, raw_instructions):
        for row in raw_instructions.splitlines():
            self.executeInstruction(row)
        return manhattan(*self.position)


example_ferry = Ferry()
u.assert_equals(example_ferry.followNavigationInstructions(example_input), 25)

ferry = Ferry()
u.answer_part_1(ferry.followNavigationInstructions(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


class FerryWithWayPoint(Ferry):
    def __init__(self):
        self.waypoint = [10, 1]
        self.position = [0, 0]

    def moveWaypointInDirection(self, direction, distance):
        self.waypoint[0] += direction[0] * distance
        self.waypoint[1] += direction[1] * distance

    def rotateWayPoint(self, angle):
        x, y = self.waypoint
        if angle == 180:
            self.waypoint = [-x, -y]
        elif angle == 90:
            self.waypoint = [-y, x]
        elif angle == 270:
            self.waypoint = [y, -x]

    def executeInstruction(self, raw_instruction):
        instruction = raw_instruction[0]
        argument = int(raw_instruction[1:])
        if instruction == "N":
            self.moveWaypointInDirection(self.DIRECTIONS[90], argument)
        elif instruction == "S":
            self.moveWaypointInDirection(self.DIRECTIONS[270], argument)
        elif instruction == "E":
            self.moveWaypointInDirection(self.DIRECTIONS[0], argument)
        elif instruction == "W":
            self.moveWaypointInDirection(self.DIRECTIONS[180], argument)
        elif instruction == "F":
            self.moveInDirection(self.waypoint, argument)
        elif instruction == "R":
            self.rotateWayPoint(-argument % 360)
        elif instruction == "L":
            self.rotateWayPoint(argument)


example_ferry = FerryWithWayPoint()
u.assert_equals(example_ferry.followNavigationInstructions(example_input), 286)

ferry = FerryWithWayPoint()
u.answer_part_2(ferry.followNavigationInstructions(raw_input))
