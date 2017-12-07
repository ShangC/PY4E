fhandle = open('mbox-short.txt')
counts = dict()
words = list()
emails = list()
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    emails.append(words[1])
for word in emails:
    counts[word] = counts.get(word, 0) + 1
print(counts)
