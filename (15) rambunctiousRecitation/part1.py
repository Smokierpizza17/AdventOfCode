with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")[0].split(",")

memory = {}
TARGETTURN = 2020


def updateMem(number, index):
    '''updates memory and changes any values necessary'''
    global memory

    if number in memory.keys():
        if len(memory[number]) == 2:
            memory[number][1] = memory[number][0]  # num in pos 0 to 1
            memory[number][0] = index  # new index to 0
        elif len(memory[number]) == 1:
            memory[number].append(memory[number][0])  # num in pos 0 to new 1
            memory[number][0] = index  # new index to 0

    else:
        memory[number] = [index]


def getNextNum(prevNum, turn):
    '''returns next number in the elf's sequence'''
    global memory
    newNum = None

    if prevNum not in memory.keys():
        newNum = 0
    else:
        if len(memory[prevNum]) == 1:
            newNum = 0
        else:
            newNum = memory[prevNum][0] - memory[prevNum][1]

    updateMem(newNum, turn)
    return newNum


prevNum = 0
currTurn = 1
for startNum in taskInput:
    updateMem(int(startNum), currTurn)
    prevNum = int(startNum)
    currTurn += 1

while currTurn < TARGETTURN + 1:
    nextNum = getNextNum(prevNum, currTurn)
    prevNum = nextNum
    currTurn += 1

print(nextNum)
