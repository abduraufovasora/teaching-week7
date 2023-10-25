FinalMarks = {"CSF": 75, "Funpro": 80, "WT": 85}
print(FinalMarks)


def calculateAverage(finalMarks):
    total = 0
    for key in finalMarks:
        total = total + finalMarks[key]
        average = total / len(finalMarks)
        return average
print(calculateAverage(FinalMarks))

module= input('Module name0')
mark= input ('Mark')
myFinalMarks(module[mark])
print(calculateAverage(myFinalMarks))

