def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y %H:%M:%S,")
    return s

def textAanmaken():
    import os
    doorgaan = 0
    if os.path.isfile('./Hardlopers.txt'):
        f = open("Hardlopers.txt", "a")
    else:
        f = open("Hardlopers.txt", "w+")
    print('Om te stoppen voer 1 in')
    while doorgaan == 0:
        naam = str(input("Voer de naam in van de hardloper: "))
        if naam == "1":
            doorgaan = 1
            f.close()
        else:
            f.write('{} {}\n'.format(strftime(), naam))

textAanmaken()