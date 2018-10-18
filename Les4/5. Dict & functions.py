import operator

def namen():
    dict = {}
    while True:
        invoer = str(input('Volgende naam: '))
        if invoer == '':
            break
        elif invoer in dict:
            for x, y in dict.items():
                if x == invoer:
                    dict[invoer] = y + 1
        else:
            dict[invoer] = 1
    dictSorted = sorted(dict.items(), key=lambda kv: kv[1])
    for x, y in dictSorted:
        if y == 1:
            print('Er is 1 student met de naam {}'.format(x))
        else:
            print('Er zijn {} studenten met de naam {}'.format(y, x))

namen()