import copy

with open("input.txt", "r") as inputFile:
    taskInput = []
    for line in inputFile.read().split("\n"):
        taskInput.append(list(line))

taskInput.pop(-1)  # removes newline at the end of the file

# used later for checking coordinates out of range
maxXCoord = len(taskInput[0]) - 1
maxYCoord = len(taskInput) - 1


def isValidCoord(Coords):
    '''Returns wether or not Coords are within the seating map'''
    xCoord = Coords[0]
    yCoord = Coords[1]
    if xCoord > maxXCoord or xCoord < 0:
        return False
    elif yCoord > maxYCoord or yCoord < 0:
        return False
    return True


def getSeat(map, coords):
    '''returns state of seat'''
    xCoord = coords[0]
    yCoord = coords[1]
    return map[yCoord][xCoord]


def printSeats(source, type="raw"):
    '''Pretty prints seats in source'''
    if type == "raw":
        for line in source:
            for i in line:
                print(i, end="")
            print("")
    elif type == "anj":
        for yCoord in range(len(source)):
            for xCoord in range(len(source[yCoord])):
                seatType = getSeat(source, (xCoord, yCoord))
                if seatType == ".":
                    print(".", end="")
                    continue
                elif seatType == "#":
                    print("#", end="")
                    continue
                numTaken = 0
                for coord in getAnjacentCoords(xCoord, yCoord):
                    if getSeat(source, coord) == "#":
                        numTaken += 1
                print(numTaken, end="")
            print("")


def getAnjacentCoords(x, y):
    '''Returns all coords immediately around given coords'''
    anjCoords = []
    anjCoords.append((x - 1, y))
    anjCoords.append((x + 1, y))
    anjCoords.append((x, y - 1))
    anjCoords.append((x, y + 1))
    anjCoords.append((x - 1, y - 1))
    anjCoords.append((x - 1, y + 1))
    anjCoords.append((x + 1, y - 1))
    anjCoords.append((x + 1, y + 1))

    combedCoords = []
    for coord in anjCoords:
        if isValidCoord(coord):
            combedCoords.append(coord)

    return combedCoords


def iterate(origTaskInput):
    '''applies rules and returns new seating layout'''
    anyChanges = False  # used to check if any changes have been made
    modTaskInput = copy.deepcopy(origTaskInput)
    for yCoord, _ in enumerate(origTaskInput):
        for xCoord, _ in enumerate(origTaskInput[yCoord]):
            seatType = getSeat(origTaskInput, (xCoord, yCoord))
            numTaken = 0

            for coord in getAnjacentCoords(xCoord, yCoord):
                if getSeat(origTaskInput, coord) == "#":
                    numTaken += 1

            if seatType == "L" and numTaken == 0:
                anyChanges = True
                modTaskInput[yCoord][xCoord] = "#"
            elif seatType == "#" and numTaken >= 4:
                anyChanges = True
                modTaskInput[yCoord][xCoord] = "L"

    if not anyChanges:
        return modTaskInput, False
    return modTaskInput, True


def countSeatsTaken(seatMap):
    '''Returns number of taken seats'''
    numTaken = 0

    for yCoord in range(len(seatMap)):
        for xCoord in range(len(seatMap[yCoord])):
            seatType = getSeat(seatMap, (xCoord, yCoord))

            if seatType == "#":
                numTaken += 1

    return numTaken


if __name__ == "__main__":
    newTaskInput = copy.deepcopy(taskInput)

    changed = True
    iterations = 0
    while changed:
        newTaskInput, changed = iterate(newTaskInput)
        iterations += 1

    printSeats(newTaskInput)
    print(countSeatsTaken(newTaskInput))
    print(iterations)
