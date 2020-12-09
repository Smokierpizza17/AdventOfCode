with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newLine at the end of the File


def toggleJmpNop(instructions, line):
    '''changes instruction from Nop to Jmp, or vice versa, returns all instr'''
    oper = instructions[line-1].split(" ")[0]
    if oper == "jmp":
        instructions[line-1] = instructions[line-1].replace("jmp", "nop")
    elif oper == "nop":
        instructions[line-1] = instructions[line-1].replace("jmp", "nop")
    else:
        raise IndexError("operation isn't JMP/NOP!")
    return instructions


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


def codeValidator(instructions):
    '''Returns the ACC value if the code finishes, otherwise False'''
    visitedLines = []
    currLine = 1
    acc = 0
    newAcc = 0
    while visitedLines.count(currLine) < 2:  # currLine can exist only once
        acc = newAcc
        deltaLine, newAcc = interpret(taskInput[currLine - 1], acc)
        currLine += deltaLine
        if currLine == len(taskInput) + 1:
            return newAcc
        visitedLines.append(currLine)
    return None


for line in range(1, len(taskInput)):
    if taskInput[line-1].split(" ")[0] == "jmp":
        newInstr = toggleJmpNop(taskInput, line)
    elif taskInput[line-1].split(" ")[0] == "nop":
        newInstr = toggleJmpNop(taskInput, line)
    else:
        continue

    if codeValidator(newInstr) is not None:
        print(codeValidator(newInstr))
