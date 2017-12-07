while True:
    try:
        fname = input('Enter file name: ')
        fhandle = open(fname)
    except:
        print('Cannot find document:"',fname,'", please try again')
    else:
        # normal code as shown in textbook
        n = 0
        rate = 0.00
        for line in fhandle:
            if line.startswith('X-DSPAM-Confidence:'):
                n += 1
                pos = line.find('0')
                rate += float(line[pos:])

        averageRate = rate/n
        print('Average spam confidence:',averageRate)
        break
