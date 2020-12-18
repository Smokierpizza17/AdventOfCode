with open("input.txt", "r") as inputFile:
    taskInput = []
    for line in inputFile.read().split("\n"):
        taskInput.append(list(line))

taskInput.pop(-1)  # removes newline at the end of the file


def getCubeState(map, coords):
    '''returns state of cube'''
    xCoord = coords[0]
    yCoord = coords[1]
    zCoord = coords[2]
    return map[zCoord][yCoord][xCoord]


def getAnjacentCoords(x, y, z):
    '''Returns all coords immediately around given coords'''
    anjCoords = []
    anjCoords.append((x - 1, y, z))
    anjCoords.append((x + 1, y, z))
    anjCoords.append((x, y - 1, z))
    anjCoords.append((x, y + 1, z))
    anjCoords.append((x - 1, y - 1, z))
    anjCoords.append((x - 1, y + 1, z))
    anjCoords.append((x + 1, y - 1, z))
    anjCoords.append((x + 1, y + 1, z))

    anjCoords.append((x - 1, y, z + 1))
    anjCoords.append((x + 1, y, z + 1))
    anjCoords.append((x, y - 1, z + 1))
    anjCoords.append((x, y + 1, z + 1))
    anjCoords.append((x - 1, y - 1, z + 1))
    anjCoords.append((x - 1, y + 1, z + 1))
    anjCoords.append((x + 1, y - 1, z + 1))
    anjCoords.append((x + 1, y + 1, z + 1))

    anjCoords.append((x - 1, y, z - 1))
    anjCoords.append((x + 1, y, z - 1))
    anjCoords.append((x, y - 1, z - 1))
    anjCoords.append((x, y + 1, z - 1))
    anjCoords.append((x - 1, y - 1, z - 1))
    anjCoords.append((x - 1, y + 1, z - 1))
    anjCoords.append((x + 1, y - 1, z - 1))
    anjCoords.append((x + 1, y + 1, z - 1))

    return anjCoords
