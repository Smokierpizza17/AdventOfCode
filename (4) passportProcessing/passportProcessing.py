with open("input.txt", "r") as inputFile:
    taskInput = []
    for passport in inputFile.read().split("\n\n"):
        taskInput.append(passport.replace("\n", " "))

taskInput.pop(-1)  # removes the newline at the end of the file


def isValidHgt(hgt):
    '''checks height according to https://adventofcode.com/2020/day/4#part2'''
    if "".join(list(hgt)[-2:]) == "cm":  # checks last two letters for "cm"
        digits = list(hgt)[:-2]
        heightNum = int("".join(digits))
        if 150 <= heightNum and heightNum <= 193:
            return True
        else:
            return False
    elif "".join(list(hgt)[-2:]) == "in":  # checks last two letters for "in"
        digits = list(hgt)[:-2]
        heightNum = int("".join(digits))
        if 59 <= heightNum and heightNum <= 76:
            return True
        else:
            return False


def isValidPid(pid):
    '''checks passport ID according to AdvOCode'''
    length = len(list(pid))
    try:
        isInt = isinstance(int(pid), int)
    except ValueError:
        return False
    if length == 9 and isInt:
        return True
    return False


def isValidHcl(hcl):
    '''checks hair colour according to AdvOCode'''
    chars = list(hcl)
    if chars[0] != "#":
        return False
    try:
        int("".join(chars[1:]), 16)
    except TypeError:
        return False
    if len(chars) == 7:
        return True
    return False


valid = 0

for passport in taskInput:
    fields = {}
    for line in passport.split(" "):
        attrib = line.split(":")[0]
        param = line.split(":")[1]
        fields[attrib] = param
    # passes if 8 attrs, or if 7 attrs with cid missing
    if len(fields) == 8 or ("cid" not in fields.keys() and len(fields) == 7):
        if int(fields["byr"]) > 2002 or 1920 > int(fields["byr"]):
            print(passport)
            print("byr invalid!")
            continue
        elif int(fields["iyr"]) > 2020 or 2010 > int(fields["iyr"]):
            print(passport)
            print("iyr invalid!")
            continue
        elif int(fields["eyr"]) > 2030 or 2020 > int(fields["eyr"]):
            print(passport)
            print("eyr invalid!")
            continue
        elif not isValidHgt(fields["hgt"]):
            print(passport)
            print("hgt invalid!")
            continue
        elif fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl",
                                   "oth"]:
            print(passport)
            print("ecl invalid!")
            continue
        elif not isValidPid(fields["pid"]):
            print(passport)
            print("pid invalid!")
            continue
        elif not isValidHcl(fields["hcl"]):
            print(passport)
            print("hcl invalid!")
            continue
        valid += 1

print(valid)
