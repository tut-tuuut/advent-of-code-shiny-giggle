import intcode as it
from PIL import Image

program = (3,8,1005,8,301,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1103,7,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,54,2,103,3,10,2,1008,6,10,1006,0,38,2,1108,7,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,91,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,114,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,136,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,158,1,1009,0,10,2,1002,18,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,187,2,1108,6,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,213,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,236,1,104,10,10,1,1002,20,10,2,1008,9,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,269,1,102,15,10,1006,0,55,2,1107,15,10,101,1,9,9,1007,9,979,10,1005,10,15,99,109,623,104,0,104,1,21102,1,932700598932,1,21102,318,1,0,1105,1,422,21102,1,937150489384,1,21102,329,1,0,1105,1,422,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,46325083227,0,1,21102,376,1,0,1106,0,422,21102,3263269927,1,1,21101,387,0,0,1105,1,422,3,10,104,0,104,0,3,10,104,0,104,0,21102,988225102184,1,1,21101,410,0,0,1105,1,422,21101,868410356500,0,1,21102,1,421,0,1106,0,422,99,109,2,21202,-1,1,1,21102,1,40,2,21102,1,453,3,21102,1,443,0,1105,1,486,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,448,449,464,4,0,1001,448,1,448,108,4,448,10,1006,10,480,1102,1,0,448,109,-2,2106,0,0,0,109,4,1201,-1,0,485,1207,-3,0,10,1006,10,503,21101,0,0,-3,22101,0,-3,1,21201,-2,0,2,21102,1,1,3,21101,0,522,0,1105,1,527,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,550,2207,-4,-2,10,1006,10,550,22102,1,-4,-4,1105,1,618,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,569,1,0,1106,0,527,22101,0,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,588,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,610,21201,-1,0,1,21101,610,0,0,105,1,485,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0)

"""
The Intcode program will serve as the brain of the robot. The program uses input instructions
to access the robot's camera: provide 0 if the robot is over a black panel or 1 if the robot
is over a white panel. Then, the program will output two values:

 -  First, it will output a value indicating the color to paint the panel the robot is over:
    0 means to paint the panel black, and 1 means to paint the panel white.
 -  Second, it will output a value indicating the direction the robot should turn:
    0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.

After the robot turns, it should always move forward exactly one panel. The robot starts facing up.
"""

class Robot:
    def __init__(self, computer):
        self.computer = computer
        self.grid = {}
        self.x = 0
        self.y = 0
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0
        self.directions = ( (0,1), (1,0), (0,-1), (-1,0) )
        self.directionIndex = 0
    
    def step(self):
        color = self.getCurrentColor()
        newColor = self.computer.run([color])
        if newColor == None:
            return False
        turn = self.computer.run([])
        self.paintIn(newColor)
        self.turn(turn)
        self.moveForward()
        return True

    
    def getCurrentColor(self):
        if (self.x, self.y) not in self.grid.keys():
            return 0
        return self.grid[(self.x, self.y)]
    
    def paintIn(self, color):
        self.grid[(self.x, self.y)] = color
    
    def turn(self, direction):
        if direction == 0:
            self.directionIndex -= 1
        elif direction == 1:
            self.directionIndex += 1
        else:
            print(f'unknown direction: {direction}')
    
    def moveForward(self):
        self.x += self.directions[self.directionIndex%4][0]
        self.y += self.directions[self.directionIndex%4][1]
        if self.x < self.minX:
            self.minX = self.x
        if self.x > self.maxX:
            self.maxX = self.x
        if self.y < self.minY:
            self.minY = self.y
        if self.y > self.maxY:
            self.maxY = self.y

def part1():
    robot = Robot(it.Computer(list(program), output_mode='return'))
    i = 0
    while robot.step():
        print(f'robot is walking... step {i}', end='\r')
        i += 1
    print(f'\n\nstep1 : robot painted {len(robot.grid.keys())} panels')

part1()

def part2():
    robot = Robot(it.Computer(list(program), output_mode='return'))
    robot.grid = {(0,0): 1}
    i = 0
    while robot.step():
        print(f'robot is walking... step {i}', end='\r')
        i += 1
    print(f'\n\nstep2 : robot painted {len(robot.grid.keys())} panels')
    print(f'will need an image of {robot.maxX - robot.minX} width x {robot.maxY - robot.minY} height')
    imgFile = Image.new('1', (robot.maxX - robot.minX + 4, robot.maxY - robot.minY + 6))
    for coords in robot.grid.keys():
        if robot.grid[coords] == 0:
            continue
        imgFile.putpixel((coords[0] - robot.minX + 2, coords[1] - robot.minY + 3), 1)
    imgFile.show()


part2()