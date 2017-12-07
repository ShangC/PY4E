while True:
    try:
        fname = input('Enter file name: ')
        fhandle = open(fname)

    except:
        print('Cannot find document:"',fname,'", please try again')
    else:
        # normal code as shown in textbook
        for line in fhandle:
            print(line.upper().rstrip())
        break
