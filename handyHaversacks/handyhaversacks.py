with open("input2.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newline at the end of the file

bags = {}  # key is a bag, def is list of sets with how often it can contain
# a different bag


def findChains(matrix, startingPoint, path=[]):
    '''returns all sequences that contain startingPoint at the start'''
    if path == []:
        path = [startingPoint]
    else:
        path.append(startingPoint)

    if startingPoint not in matrix.keys():
        print(path)
        path = []
        return

    for container in matrix[startingPoint]:
        findChains(matrix, container[0], path)


for rule in taskInput:
    splitRule = rule.split(" contain ")
    parentColour = splitRule[0].split(" bag")[0]

    subBags = []
    for subBag in splitRule[1].split(", "):
        strippedSubBags = subBag.split(" bag")[0]
        if strippedSubBags == "no other":
            subColour = None
            subNumber = 0
        else:
            subNumber = strippedSubBags[0]
            subColour = strippedSubBags[2:]
        subBags.append((subColour, subNumber))

    for bag in subBags:
        if bag[0] in bags:
            bags[bag[0]].append((parentColour, bag[1]))
        else:
            bags[bag[0]] = [(parentColour, bag[1])]

for bag in bags.keys():
    print(bag)
    print(bags[bag])

findChains(bags, "shiny gold")

# magic code, long story
allPathsWithGold = [list(leaf.path) for leaf in PreOrderIter(f, filter_=lambda node: node.is_leaf)]
