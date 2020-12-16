with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newLine at the end of the File

intTaskInput = [0]  # 0 to include airplane port
for i in taskInput:  # make list of int instead of str
    intTaskInput.append(int(i))

intTaskInput.sort()

intTaskInput.append(intTaskInput[-1] + 3)  # factor in device adapter


def splitByThreeDiffs(adapterArray):
    '''Returns list of lists, each a chain of one diff adapters'''
    finalArray = []
    currentSeries = []
    for index, adapter in enumerate(adapterArray[:-1]):
        nextAdapter = adapterArray[index + 1]
        nextDiff = nextAdapter - adapter
        currentSeries.append(adapter)
        if nextDiff == 3:
            finalArray.append(currentSeries)
            currentSeries = []
    return finalArray


nodes = 0


def countTree(map, startNum, master=False):
    global nodes
    if master:
        nodes = 0
    validAdapters = [startNum + 1, startNum + 2, startNum + 3]
    anyValid = False
    for i in validAdapters:
        if i in map:
            anyValid = True
            countTree(map, i)
    if not anyValid:
        nodes += 1
    if master:
        return nodes


splitArray = splitByThreeDiffs(intTaskInput)
runningProduct = 1

for tree in splitArray:
    nodes = countTree(tree, tree[0], True)
    runningProduct = runningProduct * countTree(tree, tree[0], True)

print("Possible adapter arrangements: %s" % runningProduct)
