import itertools

with open("input.txt", "r") as inputFile:
    taskInput = []
    for line in inputFile.readlines():
        taskInput.append(int(line.removesuffix("\n")))

# Part 1

print("PART 1")

for i in taskInput:
    if (2020 - i) in taskInput:
        print("FOUND PAIR: %s | %s" % (i, (2020 - i)))
        print("Product is %s" % (i * (2020 - i)))
        break

# Part 2

print("PART 2")

for i in itertools.combinations(taskInput, 3):
    if sum(i) == 2020:
        print(i)
        print("product is %s" % (i[0] * i[1] * i[2]))