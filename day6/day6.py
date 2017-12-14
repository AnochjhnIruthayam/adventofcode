import numpy as np
class DaySix:
    def __init__(self, file):
        self.file = file

    def loadFileToArray(self):
        with open(self.file) as f:
            return np.loadtxt(f, dtype=int).tolist()
    
    def hashList(self, list):
        hash = ""
        for element in list:
            hash += str(element)
        return hash

    def mapMemoryBank(self):
        dict = {}
        memoryBanks = self.loadFileToArray()
        dict[self.hashList(memoryBanks)] = 0
        cycleCount = 0
        while True:
            currentBank = memoryBanks.index(max(memoryBanks))
            blocks = memoryBanks[currentBank]
            memoryBanks[currentBank] = 0
            currentBank += 1
            cycleCount += 1

            for i in range(blocks):
                currentBank = currentBank % len(memoryBanks)
                memoryBanks[currentBank] += 1
                currentBank += 1
                   
            hash = self.hashList(memoryBanks)
            if hash in dict:
                return cycleCount, dict[hash]
            else:
                dict[hash] = cycleCount
    
    def partOne(self):
        return self.mapMemoryBank()[0]

    def partTwo(self):
        return self.mapMemoryBank()[0] - self.mapMemoryBank()[1]

daySix = DaySix("day6/day6puzzle.txt")

print(daySix.partOne())
print(daySix.partTwo())