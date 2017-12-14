class DayFive:
    def __init__(self, file):
        self.file = file

    def loadFileToArray(self):
        instructionSet = []
        with open(self.file) as f:
            for instruction in f:
                instructionSet.append(int(instruction))
        return instructionSet

    def partOne(self):
        instructionSet = self.loadFileToArray()
        currentInstruction = 0
        step = 0
        while currentInstruction >= 0 and currentInstruction < len(instructionSet):
            offset = instructionSet[currentInstruction]
            instructionSet[currentInstruction] += 1
            currentInstruction += offset
            step += 1
        return step

    def partTwo(self):
        instructionSet = self.loadFileToArray()
        currentInstruction = 0
        step = 0
        while currentInstruction >= 0 and currentInstruction < len(instructionSet):
            offset = instructionSet[currentInstruction]
            if offset >= 3:
                instructionSet[currentInstruction] -= 1
            else:
                instructionSet[currentInstruction] += 1
            currentInstruction += offset
            step += 1
        return step

dayFive = DayFive("day5/day5puzzle.txt")

print(dayFive.partOne())
print(dayFive.partTwo())