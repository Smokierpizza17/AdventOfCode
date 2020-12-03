# Erstellt eine 2D-Array
with open("input.txt", "r") as inputFile:
    taskInput = []
    for line in inputFile.readlines():
        taskInput.append(list(line)[0:-1])


def isTree(xCoord, yCoord, map):
    '''returns wether or not the given Position is a tree or not.'''
    if yCoord > len(taskInput)-1:
        raise IndexError("gone too far South!")
    # fange wieder von Vorne an falls X zu groß ist
    loopbackX = xCoord
    while loopbackX > len(taskInput[0])-1:
        loopbackX -= 31
    if map[yCoord][loopbackX] == "#":
        return True
    else:
        return False


def getTreeNum(deltaX, deltaY):
    '''performs part 1 given different trajectories.'''
    currentX = 0
    currentY = 0
    counter = 0
    while True:
        currentX += deltaX
        currentY += deltaY
        try:
            if isTree(currentX, currentY, taskInput):
                counter += 1
        except IndexError:
            break
    return counter


trajectories = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1

for traj in trajectories:
    treeNum = getTreeNum(traj[0], traj[1])
    product = product * treeNum
    print("%s   |   %s trees" % (traj, treeNum))

print("\nend result: %s" % (product))
