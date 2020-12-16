with open("input.txt", "r") as inputFile:
    taskInput = []
    rawFormGroups = inputFile.read().split("\n\n")
    for formGroup in rawFormGroups:
        taskInput.append(formGroup.replace("\n", " "))

taskInput[-1] = taskInput[-1].removesuffix(" ")

sum = 0

for formGroup in taskInput:
    concFormGroup = formGroup.replace(" ", "")
    letters = []
    print(concFormGroup)
    for letter in list(concFormGroup):
        if letter not in letters:
            letters.append(letter)
    print(len(letters))
    sum += len(letters)

print("Sum part 1: %s" % sum)

# part 2


def getIntersect(masterList: list[list]):
    '''returns all values that show up in all of the lists in masterList.'''
    primaryList = masterList[0]
    outputList = []
    for i in primaryList:
        for subList in masterList[1:]:
            missingFound = False
            if i not in subList:
                missingFound = True
                break
        if missingFound:
            continue
        else:
            outputList.append(i)
    return outputList


sum = 0

for formGroup in taskInput:
    print(formGroup)
    forms = formGroup.split(" ")
    if len(forms) == 1:
        concFormGroup = formGroup.replace(" ", "")
        letters = []
        print(concFormGroup)
        for letter in list(concFormGroup):
            if letter not in letters:
                letters.append(letter)
        print(len(letters))
        sum += len(letters)
        continue

    intersectLetters = getIntersect(forms)
    print(len(intersectLetters))
    sum += len(intersectLetters)

print("Sum part 2: %s" % sum)
