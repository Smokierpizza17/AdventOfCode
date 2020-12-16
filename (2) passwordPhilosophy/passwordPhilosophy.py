with open("input.txt", "r") as inputFile:
    taskInput = []
    for line in inputFile.readlines():
        taskInput.append(line.removesuffix("\n"))

# part 1


def checkpassword(minOccurence, maxOccurence, letter, password):
    '''checks that letter only occurs between min-max range in password.'''
    occurence = list(password).count(letter)
    if occurence <= maxOccurence and occurence >= minOccurence:
        return True
    return False


valid = 0

for line in taskInput:
    # splits the entries by constant dividers
    password = line.split(": ")[1]
    minOccurence = line.split(": ")[0].split("-")[0]
    maxOccurence = line.split(": ")[0].split("-")[1].split(" ")[0]
    policyLetter = line.split(": ")[0].split("-")[1].split(" ")[1]

    if checkpassword(int(minOccurence), int(maxOccurence), policyLetter,
                     password):
        valid += 1

print("valid passwords: %s" % (valid))

# part 2


def checkpassword2(pos1, pos2, letter, password):
    '''checks that letter only occurs once at pos1 and pos2 in password.'''
    correctPos1 = (password[pos1 - 1] == letter)
    correctPos2 = (password[pos2 - 1] == letter)
    if correctPos1 ^ correctPos2:
        return True
    return False


valid = 0

for line in taskInput:
    # splits the entries by constant dividers
    password = line.split(": ")[1]
    minOccurence = line.split(": ")[0].split("-")[0]
    maxOccurence = line.split(": ")[0].split("-")[1].split(" ")[0]
    policyLetter = line.split(": ")[0].split("-")[1].split(" ")[1]

    if checkpassword2(int(minOccurence), int(maxOccurence), policyLetter,
                      password):
        valid += 1

print("valid passwords 2: %s" % (valid))
