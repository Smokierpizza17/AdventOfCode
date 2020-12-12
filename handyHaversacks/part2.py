with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # removes newline at the end of the file

childFinder = {}  # key is a bag, def is list of sets with how often it
# contain in a different bag
objectFinder = {}  # key is colour, def is bag object of colour


class bag():
    def __init__(self, colour, subBags):
        self.colour = colour
        self.subBags = subBags
        objectFinder[colour] = self


def generateObjects(map):
    '''fills objectFinder with values'''
    for colour in map.keys():
        bag(colour, map[colour])


def containerTree(map, startingPoint):
    '''Returns number of bags that startingPoint contains'''
    subBags = map[startingPoint].subBags
    bagCounter = 1  # including self
    if len(subBags) == 0:
        return bagCounter

    for bag, count in subBags:
        bagCounter += containerTree(map, bag) * count

    return bagCounter


for rule in taskInput:
    splitRule = rule.split(" contain ")
    parentColour = splitRule[0].split(" bag")[0]

    subbags = []
    for subBag in splitRule[1].split(", "):
        strippedsubbags = subBag.split(" bag")[0]
        if strippedsubbags == "no other":
            continue
        else:
            subNumber = int(strippedsubbags[0])
            subColour = strippedsubbags[2:]
        subbags.append((subColour, subNumber))

    childFinder[parentColour] = subbags

generateObjects(childFinder)
print(containerTree(objectFinder, "shiny gold") - 1)  # don't want to count top
# level bag
