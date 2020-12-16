with open("input.txt", "r") as inputFile:
    taskInput = inputFile.read().split("\n")

taskInput.pop(-1)  # remove newline at end of file

objectMap = {}


class shuttle():
    def __init__(self, id, listPos):
        self.id = id
        self.listPos = listPos
        objectMap[id] = self

    def departs(self, time):
        '''Returns True/False wether or not the bus departs at timestamp'''
        if time % self.id == 0:
            return True
        else:
            return False


startTime = int(taskInput[0])

for i, bus in enumerate(taskInput[1].split(",")):
    if bus == "x":
        continue
    print(bus)
    shuttle(int(bus), i)

busFound = None
timeAfterStart = -1  # start of loop adds 1, want to start at startTime
while busFound is None:
    timeAfterStart += 1
    for bus in objectMap.values():
        if bus.departs(timeAfterStart + startTime):
            busFound = bus.id

print("bus with id %s comes %smin after start: product is %s" %
      (busFound, timeAfterStart, busFound * timeAfterStart))
