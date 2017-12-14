class DayFour:
    def __init__(self, file):
        self.file = file

    def partOne(self):
        dict = {}
        vaildCount = 0
        with open(self.file) as f:
            for line in f:
                for word in line.split():
                    if word in dict:
                        dict[word] += 1
                    else:
                        dict[word] = 1
                if len(dict.values()) == len(line.split()):
                    vaildCount += 1
                dict.clear()
        return vaildCount

    def partTwo(self):
        dict = {}
        vaildCount = 0
        with open(self.file) as f:
            for line in f:
                for word in line.split():
                    alphaSortedWord = ''.join(sorted(word))
                    if alphaSortedWord in dict:
                        dict[alphaSortedWord] += 1
                    else:
                        dict[alphaSortedWord] = 1
                if len(dict.values()) == len(line.split()):
                    vaildCount += 1
                dict.clear()
        return vaildCount

dayFour = DayFour("day4puzzle.txt")

print(dayFour.partOne())
print(dayFour.partTwo())