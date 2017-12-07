fhandle = open('mbox-short.txt')
counts = dict()
words = list()
emails = list()
largest = None
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    emails.append(words[1])
for word in emails:
    counts[word] = counts.get(word, 0) + 1
for email in emails:
    if largest is None or counts[email] > largest:
        largest = counts[email]
print(email,largest)
# add line to try Git
