# the first time, I try to search line.startswith('From') without the space, which leads to 54 lines of search result. 

fileHandle = open('mbox-short.txt')
count = 0
for line in fileHandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    count += 1
    print(words[1])
print('There were', count, 'lines in the file with From as the first word')
