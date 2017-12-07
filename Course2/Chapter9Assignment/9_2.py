import string
fhandle = open('mbox-short.txt')
counts = dict()
words = list()
holiday = list()
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    holiday.append(words[2])
for word in holiday:
    counts[word] = counts.get(word, 0) + 1
print(counts)
