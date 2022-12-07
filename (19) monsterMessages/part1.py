with open("testinput.txt", "r") as inputFile:
    inputGroups = inputFile.read().split("\n\n")

rules = inputGroups[0].split("\n")
messages = inputGroups[1].split("\n")

messages.pop(-1)  # remove newline at end of file

ruleDict = {}

for rule in rules:
    ruleName = rule.split(": ")[0]
    rulePointers = rule.split(": ")[1].split(" | ")
