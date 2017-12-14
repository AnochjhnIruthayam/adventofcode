import math

class DayThree:
    x = 0
    y = 0

    currentMove = 0
    def __init__(self, squareIndex):
        self.squareIndex = squareIndex

    def up(self):
        self.y += 1

    def down(self):
        self.y -=1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def reset(self):
        self.x = 0
        self.y = 0
        self.currentMove = 0
    
    def makeMove(self):
        switcher = {
            0: self.right,
            1: self.up,
            2: self.left,
            3: self.down
        }
        func = switcher.get(self.currentMove, lambda: "Move does not exist")
        func()

    def nextMove(self):
        self.currentMove = (self.currentMove + 1) % 4

    def adjacentSum(self, dict, x, y):
        sum = 0
        if (x,y+1) in dict:
            sum +=dict[(x,y+1)]
        if (x+1, y+1) in dict:
            sum +=dict[(x+1, y+1)]
        if (x+1, y) in dict:
            sum +=dict[(x+1,y)]
        if (x+1, y-1) in dict:
            sum +=dict[(x+1,y-1)]
        if (x, y-1) in dict:
            sum +=dict[(x,y-1)]
        if (x-1, y-1) in dict:
            sum +=dict[(x-1,y-1)]
        if (x-1, y) in dict:
            sum +=dict[(x-1,y)]
        if (x-1, y+1) in dict:
            sum +=dict[(x-1,y+1)]

        return sum

    def partOne(self):
        self.reset()
        stepSize = 1
        count = 0
        for i in range(2, self.squareIndex+1):
            self.makeMove()
            count += 1
            if count == stepSize:
                self.nextMove()
                continue
            if count == (stepSize * 2):
                self.nextMove()
                stepSize += 1
                count = 0
        return int( math.sqrt( pow( (self.x - 0), 2 ) ) + math.sqrt( pow( (self.y -0), 2 ) ) )

    def partTwo(self):
        self.reset()
        stepSize = 1
        count = 0
        temp = 0
        dict = {}
        dict[(self.x, self.y)] = 1
        while self.squareIndex+1 > temp:
            self.makeMove()
            temp = self.adjacentSum(dict, self.x, self.y)
            dict[(self.x, self.y)] = temp
            count += 1
            if count == stepSize:
                self.nextMove()
                continue
            if count == (stepSize * 2):
                self.nextMove()
                stepSize += 1
                count = 0
        return dict[(self.x, self.y)]


dayThree = DayThree(325489)

print(dayThree.partOne())
print(dayThree.partTwo())
