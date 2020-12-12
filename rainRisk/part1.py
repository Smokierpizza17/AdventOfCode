with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newline at end of file

DIRMODIFIERS = ["L", "R"]
ABSMOVERS = ["N", "S", "E", "W"]

shipFacing = 1  # N=0, E=1, S=2, W=3
shipECoord = 0
shipNCoord = 0


def interpret(instruction):
    '''interprets instruction and changes ship's values'''
    global DIRMODIFIERS
    global ABSMOVERS
    global shipFacing
    global shipECoord
    global shipNCoord

    operator = instruction[0]
    value = int(instruction[1:])

    if operator in DIRMODIFIERS:
        if operator == "R":
            rotator = value / 90
        elif operator == "L":
            rotator = -(value / 90)
        newDir = (shipFacing + rotator) % 4
        shipFacing = newDir
    elif operator in ABSMOVERS:
        if operator == "E":
            shipECoord += value
        elif operator == "W":
            shipECoord -= value
        elif operator == "N":
            shipNCoord += value
        elif operator == "S":
            shipNCoord -= value
    else:  # must be "F"
        if shipFacing == 1:
            shipECoord += value
        elif shipFacing == 2:
            shipNCoord -= value
        elif shipFacing == 3:
            shipECoord -= value
        elif shipFacing == 0:
            shipNCoord += value


def getManhattanDistance():
    '''returns Manhattan distance of ship'''
    global shipECoord
    global shipNCoord

    absNS = abs(shipNCoord)
    absEW = abs(shipECoord)

    return absNS + absEW


for line in taskInput:
    interpret(line)

print("Manhattan distance: %s" % getManhattanDistance())
