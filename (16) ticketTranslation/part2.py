import re

with open("input.txt", "r") as inputFile:
    inputGroups = inputFile.read().split("\n\n")

inputLines = []
for i in inputGroups:
    inputLines.append(i.split("\n"))

inputLines[2].pop(0)  # remove "nearby tickets:" from lines
inputLines[2].pop(-1)  # remove newline at the end of the file

myTicket = inputLines[1][1].split(",")  # group 2, avoid "my ticket:"
print(myTicket)
ruleDict = {}  # key is attribute, value is list of ranges that are valid

allAttr = []


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


def isAllValid(values):
    '''returns True if all values are True, else False'''
    for value in values:
        if value is False:
            return False
    return True


for rule in inputLines[0]:
    getAttrib = re.compile(r".+?(?=:)")
    attrib = re.findall(getAttrib, rule)[0]
    allAttr.append(attrib)

    getRangevalues = re.compile(r"\d+")
    rangeValues = re.findall(getRangevalues, rule)
    rangeValues = iter(rangeValues)

    ranges = []
    for value in rangeValues:
        ranges.append(range(int(value), int(next(rangeValues))+1))

    ruleDict[attrib] = ranges

combedTickets = []
for ticket in inputLines[2]:
    values = ticket.split(",")
    ticketValid = True
    for value in values:
        value = int(value)
        if not isWithinAnyRange(value):
            ticketValid = False
            break
    if ticketValid:
        combedTickets.append(values)

indexAttrMap = {}
for index in range(len(combedTickets[0])):
    attrMap = {}
    for attrib in ruleDict.keys():
        validArray = []
        for ticket in combedTickets:
            param = int(ticket[index])
            validArray.append(isWithinAttribRange(attrib, param))
        allValid = isAllValid(validArray)
        attrMap[attrib] = allValid
    indexAttrMap[index] = attrMap

assignedAttr = {}
while len(assignedAttr) != len(allAttr):
    for index, attrMap in indexAttrMap.items():
        latestTrueAttr = None
        numAllTrue = 0
        for attr, allTrue in attrMap.items():
            if attr in assignedAttr.values():
                continue
            if allTrue:
                numAllTrue += 1
                latestTrueAttr = attr
        if numAllTrue == 1:
            assignedAttr[index] = latestTrueAttr

finalProduct = 1  # because times
for index, attr in assignedAttr.items():
    print(attr)
    if "departure" in attr:
        value = int(myTicket[index])
        finalProduct = finalProduct * value

print("final product is %s" % finalProduct)
