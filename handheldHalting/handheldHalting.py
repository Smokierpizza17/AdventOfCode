with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newLine at the end of the File


def toggleJmpNop(instructions, line):
    '''changes instruction from Nop to Jmp, or vice versa, returns all instr'''
    tmpInstr = []
    for i in instructions:
        tmpInstr.append(i)

    oper = instructions[line].split(" ")[0]
    if oper == "jmp":
        tmpInstr[line] = tmpInstr[line].replace("jmp", "nop")
    elif oper == "nop":
        tmpInstr[line] = tmpInstr[line].replace("nop", "jmp")
    else:
        raise IndexError("operation isn't JMP/NOP!")
    return tmpInstr


def interpret(instruction, acc):
    '''performs instruction and returns nextLineDelta AND newAccValue'''
    oper = instruction.split(" ")[0]
    arg = instruction.split(" ")[1]
    if oper == "nop":
        return 1, acc
    elif oper == "jmp":
        return int(arg), acc
    elif oper == "acc":
        return 1, acc + int(arg)


def codeValidator(checkInstr):
    '''Returns the ACC value if the code finishes, otherwise False'''
    visitedLines = []
    currLine = 0
    acc = 0
    newAcc = 0
    while visitedLines.count(currLine) < 2:  # currLine can exist only once
        acc = newAcc
        deltaLine, newAcc = interpret(checkInstr[currLine], acc)
        currLine += deltaLine

        if deltaLine == 0:  # jmp 0 indicates loop
            return None

        if currLine == len(checkInstr):  # if at the end of the file
            return newAcc
        visitedLines.append(currLine)
    return None


for line in range(0, len(taskInput)):
    if taskInput[line].split(" ")[0] == "jmp":
        newInstr = toggleJmpNop(taskInput, line)
    elif taskInput[line].split(" ")[0] == "nop":
        newInstr = toggleJmpNop(taskInput, line)
    else:
        continue
    acc = codeValidator(newInstr)
    if acc is not None:
        print(acc)
