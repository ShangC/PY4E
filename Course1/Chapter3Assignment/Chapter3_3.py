class InvalidNumberError(Exception):
    #for typing number that is greater than 1
    pass

while True:
    try:
        score = input('Enter Score:')
        fs = float(score)
        if fs < 0.0 or fs > 1.0:
            raise InvalidNumberError
    except ValueError:
        print ('Invalid character, please try again')
    except InvalidNumberError:
        print('Value out of range, please try again')
    else:
        if fs >= 0.9 and fs <= 1.0:
            print('A')
        elif fs >= 0.8 and fs < 0.9:
            print('B')
        elif fs >= 0.7 and fs < 0.8:
            print('C')
        elif fs >= 0.6 and fs < 0.7:
            print('D')
        else:
            print('F')
        break
