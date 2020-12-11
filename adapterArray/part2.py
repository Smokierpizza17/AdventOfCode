with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newLine at the end of the File

intTaskInput = [0]  # 0 to include airplane port
for i in taskInput:  # make list of int instead of str
    intTaskInput.append(int(i))

intTaskInput.sort()

intTaskInput.append(intTaskInput[-1] + 3)  # factor in device adapter

endNodeCounter = 0


def genTreeStep(startNum):
    global endNodeCounter
    validAdapters = [startNum + 1, startNum + 2, startNum + 3]
    anyValid = False
    for i in validAdapters:
        if i in intTaskInput:
            anyValid = True
            genTreeStep(i)
    if not anyValid:
        endNodeCounter += 1
        if endNodeCounter % 1000000 == 0:
            print(endNodeCounter / 1000000000000)


genTreeStep(0)

print(endNodeCounter)
