fileHandle = open('romeo.txt')
firstList = list()
for line in fileHandle:
    firstList += line.rstrip().split()
firstList.sort()
secondList = list()
for item in firstList:
    if item not in secondList:
        secondList.append(item)
secondList.sort()
print(secondList)
