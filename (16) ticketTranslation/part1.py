import re

with open("input.txt", "r") as inputFile:
    inputGroups = inputFile.read().split("\n\n")

inputLines = []
for i in inputGroups:
    inputLines.append(i.split("\n"))

inputLines[2].pop(0)  # remove "nearby tickets:" from lines
inputLines[2].pop(-1)  # remove newline at the end of the file

ruleDict = {}  # key is attribute, value is list of ranges that are valid


def isWithinAttribRange(attribName, value):
    '''check if value is in the ranges specified in attribName'''
    global ruleDict
    for range in ruleDict[attribName]:
        if value in range:
            return True
    return False


def isWithinAnyRange(value):
    '''check if value is in any range specified in ruleDict'''
    global ruleDict
    for attrib in ruleDict.keys():
        if isWithinAttribRange(attrib, value):
            return True
    return False


for rule in inputLines[0]:
    getAttrib = re.compile(r".+?(?=:)")
    attrib = re.findall(getAttrib, rule)[0]

    getRangevalues = re.compile(r"\d+")
    rangeValues = re.findall(getRangevalues, rule)
    rangeValues = iter(rangeValues)

    ranges = []
    for value in rangeValues:
        ranges.append(range(int(value), int(next(rangeValues))+1))

    ruleDict[attrib] = ranges

invalidValuesSum = 0
for ticket in inputLines[2]:
    values = ticket.split(",")
    for value in values:
        value = int(value)
        if not isWithinAnyRange(value):
            invalidValuesSum += value
            break

print("ticket scanning error rate is %s" % (invalidValuesSum))
