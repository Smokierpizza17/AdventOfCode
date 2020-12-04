with open("input.txt", "r") as inputFile:
    taskInput = []
    for passport in inputFile.read().split("\n\n"):
        taskInput.append(passport.replace("\n", " "))

valid = 0

for password in taskInput:
    fields = {}
    for line in password.split(" "):
        attrib = line.split(":")[0]
        param = line.split(":")[1]
        fields[attrib] = param
    if len(fields) == 8 or ("cid" not in fields.keys() and len(fields) == 7):
        valid += 1

print(valid)
