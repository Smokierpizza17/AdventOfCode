with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newline at the end of the file

parentFinder = {}  # key is a bag, def is list of sets with how often it can be
# in a different bag
childFinder  = {}  # key is a bag, def is list of sets with how often it
# contain in a different bag


def findChains(matrix, startingPoint, bags=[], master=False):
    '''returns all bags that can contain startingPoint'''
    if startingPoint not in matrix:
        return
    for parentBag in matrix[startingPoint]:
        parentColour = parentBag[0]
        if parentColour not in bags:
            bags.append(parentColour)
            findChains(matrix, parentColour, bags)
    if master:
        return bags


for rule in taskInput:
    splitRule = rule.split(" contain ")
    parentColour = splitRule[0].split(" bag")[0]

    subbags = []
    for subBag in splitRule[1].split(", "):
        strippedsubbags = subBag.split(" bag")[0]
        if strippedsubbags == "no other":
            subColour = None
            subNumber = 0
        else:
            subNumber = strippedsubbags[0]
            subColour = strippedsubbags[2:]
        subbags.append((subColour, subNumber))

    for bag in subbags:
        if bag[0] in parentFinder:
            parentFinder[bag[0]].append((parentColour, bag[1]))
        else:
            parentFinder[bag[0]] = [(parentColour, bag[1])]
    childFinder[parentColour] = subbags
    

print(len(findChains(parentFinder, "shiny gold", master=True)))
