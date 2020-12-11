import copy, part1

#functions used for part two
def read_file_into_object(filename):
    seatLayout = []
    with open(filename) as fp:
        line = fp.readline()
        cnt = 0
        seatLayout.append([])
        while line:
            line = list(line)
            for i in range(len(line)-1):
                newSeat = Seat(line[i])
                seatLayout[cnt].append(newSeat)
            line = fp.readline()
            cnt += 1
            seatLayout.append([])
    return seatLayout[:-1]

class Seat:
    def __init__(self, floor):
        self.edgeCase = False
        self.firstNeighborPerDirection = []
        if floor == ".":
            self.floor = True
            self.sign = "."
        else:
            self.floor = False
            self.sign = "#"
        self.occupied = [True, True]

    def addNeighbor(self, i, j):
        self.firstNeighborPerDirection.append([i, j])

    def isTaken(self, iteration):
        return self.occupied[iteration]

def find_edge_cases_and_first_changeable_neighbors(seatLayout):
    rows = len(seatLayout)
    columns = len(seatLayout[0])
    totalOccupiedSeats = 0
    directions = [[0,-1], [-1,0], [0,1], [1,0], [-1,-1], [1,1], [-1,1], [1,-1]]
    for i in range(rows):
        for j in range(columns):
            if seatLayout[i][j].floor:
                continue
            totalOccupiedSeats = totalOccupiedSeats + 1
            neighboursAdded = 0
            for newx, newy in directions:
                x, y = i+newx, j+newy
                while (0 <= x < rows) and (0 <= y < columns):
                    if seatLayout[x][y].floor == False:
                        seatLayout[i][j].addNeighbor(x, y)
                        neighboursAdded = neighboursAdded + 1
                        break
                    x, y = x + newx, y + newy
            if neighboursAdded < 5:
                seatLayout[i][j].edgeCase = True
                seatLayout[i][j].occupied[1] = True
    return seatLayout, totalOccupiedSeats

def simulate_seats_part_two(seatLayout, totalOccupiedSeats):
    rows = len(seatLayout)
    columns = len(seatLayout[0])
    iteration = 0
    seatChangesLastIteration = True
    howManyTimes = 0

    while seatChangesLastIteration:
        howManyTimes = howManyTimes +1
        seatChangesLastIteration = False

        for i in range(rows):
            for j in range(columns):
                if seatLayout[i][j].floor == True:
                    continue
                if seatLayout[i][j].edgeCase == True:
                    continue
                occupiedNeighborSeats = 0
                for neighbourx, neighboury in seatLayout[i][j].firstNeighborPerDirection:
                    if seatLayout[neighbourx][neighboury].occupied[iteration]:
                        occupiedNeighborSeats = occupiedNeighborSeats + 1
                if seatLayout[i][j].occupied[iteration]:
                    if occupiedNeighborSeats >= 5:
                        seatChangesLastIteration = True
                        seatLayout[i][j].occupied[(iteration+1)%2] = False
                        seatLayout[i][j].sign = "L"
                        totalOccupiedSeats = totalOccupiedSeats - 1
                    else:
                        seatLayout[i][j].occupied[(iteration+1)%2] = seatLayout[i][j].occupied[iteration]
                else:
                    if occupiedNeighborSeats == 0:
                        seatChangesLastIteration = True
                        seatLayout[i][j].occupied[(iteration+1)%2] = True
                        seatLayout[i][j].sign = "#"
                        totalOccupiedSeats = totalOccupiedSeats + 1
                    else:
                        seatLayout[i][j].occupied[(iteration+1)%2] = seatLayout[i][j].occupied[iteration]
        iteration = (iteration+1)%2

    return totalOccupiedSeats

def print_seat_layout(seatLayout):
    rows = len(seatLayout)
    columns = len(seatLayout)
    for i in range(rows):
        row = ""
        for j in range(columns):
            row = row + seatLayout[i][j].sign
        print(row)

def print_seat_layout_iteration(seatLayout, iteration):
    rows = len(seatLayout)
    columns = len(seatLayout)
    for i in range(rows):
        row = ""
        for j in range(columns):
            if seatLayout[i][j].floor == True:
                row = row + "."
            else:
                row = row + str(int(seatLayout[i][j].occupied[iteration]))
        print(row)

def part_two():
    seatLayout = read_file_into_object("input")
    seatLayout, totalOccupiedSeats = find_edge_cases_and_first_changeable_neighbors(seatLayout)
    return simulate_seats_part_two(seatLayout, totalOccupiedSeats)


# functions used for part one
def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data[:-1]

def get_occupied_adjacent_seats(seatx, seaty, seatLayout):
    occupiedAdjacentSeats = 0
    if seatLayout[seatx][seaty-1] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx][seaty+1] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx-1][seaty] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx+1][seaty] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx-1][seaty-1] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx+1][seaty+1] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx+1][seaty-1] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    if seatLayout[seatx-1][seaty+1] == "#":
        occupiedAdjacentSeats = occupiedAdjacentSeats + 1
    return occupiedAdjacentSeats


def simulate_seats(seatLayout, totalOccupiedSeats):
    global iterations
    iterations += 1
    nextSeatLayout = copy.deepcopy(seatLayout)
    seatRowsNumber = len(seatLayout)-1
    seatColumnsNumber = len(seatLayout[0])-1
    for i in range(1, seatRowsNumber):
        for j in range(1, seatColumnsNumber):
            occupiedAdjacentSeats = get_occupied_adjacent_seats(i, j, seatLayout)
            if seatLayout[i][j] == "L":
                if occupiedAdjacentSeats == 0:
                    nextSeatLayout[i][j] = "#"
                    totalOccupiedSeats = totalOccupiedSeats + 1
            if seatLayout[i][j] == "#":
                if occupiedAdjacentSeats >= 4:
                    nextSeatLayout[i][j] = "L"
                    totalOccupiedSeats = totalOccupiedSeats - 1
    part1.printSeats(nextSeatLayout)
    part1.countSeatsTaken(nextSeatLayout)
    print(totalOccupiedSeats)
    return totalOccupiedSeats
    

def add_floor_padding_and_turn_to_matrix(seatLayout):
    floorRow = ["." for i in range(len(seatLayout[0])+2)]
    for row in range(0, len(seatLayout)):
        seatLayout[row] = list("." + seatLayout[row] + ".")
    seatLayout.insert(0, floorRow)
    seatLayout.append(floorRow)
    return seatLayout

def part_one():
    seatLayout = read_file("input.txt").split("\n")
    seatLayout = add_floor_padding_and_turn_to_matrix(seatLayout)
    return simulate_seats(seatLayout, 0)

print(part_one())
# print(part_two())

