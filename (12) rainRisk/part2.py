with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newline at end of file

DIRMODIFIERS = ["L", "R"]
ABSMOVERS = ["N", "S", "E", "W"]

shipFacing = 1  # N=0, E=1, S=2, W=3
shipECoord = 0
shipNCoord = 0

waypointECoord = 10
waypointNCoord = 1


def interpretRotators(dir, degrees):
    '''interprets L/R instruction and changes waypoint's values'''
    global waypointECoord
    global waypointNCoord

    rotator = int(degrees / 90)
    for _ in range(rotator):
        oldE = waypointECoord
        oldN = waypointNCoord
        if dir == "R":
            waypointNCoord = - oldE
            waypointECoord = oldN
        else:
            waypointNCoord = oldE
            waypointECoord = - oldN


def interpret(instruction):
    '''interprets instruction and changes ship's values'''
    global DIRMODIFIERS
    global ABSMOVERS
    global shipFacing
    global shipECoord
    global shipNCoord
    global waypointNCoord
    global waypointECoord

    operator = instruction[0]
    value = int(instruction[1:])

    if operator in DIRMODIFIERS:
        interpretRotators(operator, value)
    elif operator in ABSMOVERS:
        if operator == "E":
            waypointECoord += value
        elif operator == "W":
            waypointECoord -= value
        elif operator == "N":
            waypointNCoord += value
        elif operator == "S":
            waypointNCoord -= value
    else:  # must be "F"
        shipECoord += waypointECoord * value
        shipNCoord += waypointNCoord * value


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
