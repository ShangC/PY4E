fhandle = open('mbox-short.txt')

hour_histogram = {}
tuple_list = []


for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    time = line.split()[5]
    hour = time.split(':')[0]
    hour_histogram[hour] = hour_histogram.get(hour, 0) + 1

for key in hour_histogram:
    tuple_list.append((key, hour_histogram[key])



for item in list_sort:
    print(item)