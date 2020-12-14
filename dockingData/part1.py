import re

with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # remove newline at end of file


def applyBitmask(bitMask, bitStr):
    '''returns bitStr with bitmask applied'''
    maskMap = {}
    for index, value in enumerate(bitMask):
        if value != "X":
            maskMap[index] = value

    outStr = list(bitStr)
    for index, value in enumerate(bitStr):
        if index in maskMap.keys():
            outStr[index] = maskMap[index]
    return "".join(outStr)


def intToBitStr(inputInt):
    '''converts int to 36-digit bitString'''
    rawBinary = bin(inputInt).removeprefix("0b")
    while len(rawBinary) != 36:
        rawBinary = "0" + rawBinary
    return rawBinary


def bitStrToInt(bitStr):
    '''converts binary number as string to integer'''
    return int(bitStr, 2)


bitmask = ""
memory = {}
for line in taskInput:
    operator = line.split(" = ")[0]
    value = line.split(" = ")[1]
    if operator == "mask":
        bitmask = value
        continue
    elif operator.startswith("mem"):
        adress = int(re.findall(r"\d+", operator)[0])
        BinAdress = intToBitStr(adress)
        BinValue = intToBitStr(int(value))
        memory[BinAdress] = applyBitmask(bitmask, BinValue)

sum = 0
for val in memory.values():
    sum += bitStrToInt(val)

print("Sum is %s" % sum)
