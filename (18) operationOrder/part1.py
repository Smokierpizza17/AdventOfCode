import re

with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # remove newline at the end of file


bracketContents = re.compile(r"(?<=\()[^\(\)]*(?=\))")  # magick
fullExpression = re.compile(r"\d+ [\+|\*] \d+")  # magick
firstOperandFromExp = re.compile(r"\d+(?=[ \+| \*])")  # magick
secondOperandFromExp = re.compile(r"(?<=[\+ |\* ])\d+")  # magick
operatorFromExp = re.compile(r"[\*|\+]")  # magick


def interpret(line):
    '''returns value of given maths expression'''
    # check and evaluate brackets
    global bracketContents
    global fullExpression
    global firstOperandFromExp
    global secondOperandFromExp
    global operatorFromExp

    while "(" in line:
        inlaidBrackets = re.findall(bracketContents, line)  # LTR
        for content in inlaidBrackets:
            value = interpret(content)
            contentWithBrackets = "(%s)" % content
            line = line.replace(contentWithBrackets, str(value), 1)

    while len(re.findall(operatorFromExp, line)) != 0:  # while operators still
        # there
        fullExp = re.findall(fullExpression, line)[0]
        val1 = re.findall(firstOperandFromExp, fullExp)[0]
        oper = re.findall(operatorFromExp, fullExp)[0]
        val2 = re.findall(secondOperandFromExp, fullExp)[0]

        if oper == "+":
            value = int(val1) + int(val2)
            line = line.replace(fullExp, str(value), 1)
        elif oper == "*":
            value = int(val1) * int(val2)
            line = line.replace(fullExp, str(value), 1)

    return line


sum = 0
for line in taskInput:
    sum += int(interpret(line))

print("sum is %s" % sum)
