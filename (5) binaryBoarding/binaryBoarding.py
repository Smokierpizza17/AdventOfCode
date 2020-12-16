import math

with open("input.txt", "r") as inputFile:
    taskInput = []
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes the newline at the end of the file


def getRowCol(boardPass):
    '''returns a set of Row and Column from a binary boarding pass.'''
    maxRow = 127
    minRow = 0
    instructions = list(boardPass)
    for i in instructions[:7]:
        divider = (maxRow + minRow) / 2
        if i == "F":
            divider = math.floor(divider)
            maxRow = divider
        elif i == "B":
            divider = math.ceil(divider)
            minRow = divider
        else:
            print("too many instructions!")
    row = maxRow

    maxCol = 7
    minCol = 0

    for i in instructions[7:]:
        divider = (maxCol + minCol) / 2
        if i == "L":
            divider = math.floor(divider)
            maxCol = divider
        elif i == "R":
            divider = math.ceil(divider)
            minCol = divider
        else:
            print("too many instructions!")
    col = maxCol

    return (row, col)


def getSeatID(coords):
    '''returns (r * 8) + c'''
    return coords[0] * 8 + coords[1]


seatCoordsLeft = []
for r in range(0, 128):
    for c in range(0, 8):
        seatCoordsLeft.append((r, c))

seatIDs = []
for i in taskInput:
    coords = getRowCol(i)
    seatCoordsLeft.remove(coords)
    seatID = getSeatID(coords)
    seatIDs.append(seatID)

for i in seatCoordsLeft:
    seatID = getSeatID(i)
    if seatID - 1 not in seatIDs:
        continue
    elif seatID + 1 not in seatIDs:
        continue
    else:
        print(seatID)
