def programma():
    uitkomst = 0
    aantalLoops = 0
    while True:
        invoer = int(input('Voer een getal in: '))
        if invoer != 0:
            uitkomst = uitkomst + invoer
            aantalLoops = aantalLoops + 1
        else:
            break
    print('Er zijn {} getallen ingevoerd, de som is {}'.format(aantalLoops, uitkomst))

programma()