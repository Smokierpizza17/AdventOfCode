with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newLine at the end of the File

PREAMBLE = 25

# turns all input data into integers
intTaskInput = []
for i in taskInput:
    intTaskInput.append(int(i))


def isValid(num, preamble):
    '''Returns True/False, depending on wether or not num is the sum of two
    numbers from the preamble'''
    for summand in preamble:
        if num - summand in preamble:
            return True
    return False


def getSum(stream, lower=None, upper=None):
    '''Returns the Sum of all ints between lower and upper in stream'''
    sum = 0
    if lower is not None:
        for i in stream[lower:upper]:
            sum += i
    else:
        for i in stream:
            sum += i
    return sum


def getSumPreRange(intTaskInput, checkNum):
    '''returns contiguous list of numbers that add up to checkNum'''
    for lower in range(len(intTaskInput)):
        for upper in range(lower, len(intTaskInput)):
            sum = getSum(intTaskInput, lower, upper)
            if sum < checkNum:
                continue  # go to next upper value
            elif sum > checkNum:
                break  # stop checking upper, go to next lower
            else:
                return intTaskInput[lower:upper]


for index in range(25, len(intTaskInput)):
    checkNum = intTaskInput[index]
    preamble = intTaskInput[index - PREAMBLE:index]

    if not isValid(checkNum, preamble):
        print("INVALID at index %s: %s" % (index, checkNum))

        sumPreRange = getSumPreRange(intTaskInput, checkNum)
        minPreamble = sumPreRange[0]
        maxPreamble = sumPreRange[0]
        print(sumPreRange)
        for preamb in sumPreRange:
            if preamb < minPreamble:
                minPreamble = preamb
                continue
            elif preamb > maxPreamble:
                maxPreamble = preamb
                continue

        encWeakness = minPreamble + maxPreamble
        print("sum of %s and %s: %s" % (minPreamble, maxPreamble, encWeakness))
