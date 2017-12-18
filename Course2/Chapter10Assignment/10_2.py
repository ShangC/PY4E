fhandle = open('mbox-short.txt')

dic = dict()
hourList = []
for line in fhandle:
    if not line.startswith('From '):
        continue
    line = line.rstrip()
    lineItem = line.split()
    #print(lineItem)
    lineTime = lineItem[5]
    #print(lineTime)
    timeItem = lineTime.split(':')
    #print(timeItem)
    hour = timeItem[0]
    #print(hours)
    dic[hour] = dic.get(hour,0)+1

 
for hour, count in dic.items():
    hourList.append((hour, count))

hourList.sort()

for hour, count in hourList:
    print(hour, count)