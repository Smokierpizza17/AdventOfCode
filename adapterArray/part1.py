from typing import Type


with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newLine at the end of the File

intTaskInput = [0]  # 0 to include airplane port
for i in taskInput:  # make list of int instead of str
    intTaskInput.append(int(i))

intTaskInput.sort()

intTaskInput.append(intTaskInput[-1] + 3)  # factor in device adapter

oneDiffCounter = 0
threeDiffCoutner = 0
for i in range(1, len(intTaskInput)):
    curr = intTaskInput[i]
    prev = intTaskInput[i - 1]
    diff = curr - prev

    if diff == 1:
        oneDiffCounter += 1
    elif diff == 3:
        threeDiffCoutner += 1
    else:
        raise TypeError("difference other than one or three found!")

print("one diffs: %s" % oneDiffCounter)
print("three difs : %s" % threeDiffCoutner)
print("product: %s" % (oneDiffCounter * threeDiffCoutner))
