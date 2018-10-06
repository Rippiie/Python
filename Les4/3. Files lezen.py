def kaartmaker():
    infile = open('Kaartnummers.txt', 'r')
    content = infile.readlines()
    infile.close()
    maxGetal = 0
    regelNummer = 0
    for line in content:
        var = line.split(',')
        regelNummer = regelNummer + 1
        if int(var[0]) > maxGetal:
            maxGetal = int(var[0])
            nummerGoed = regelNummer
    print('Deze file telt {} regels \nHet grootste kaartnummer is: {} en dat staat op regel {}'.format(regelNummer, maxGetal, nummerGoed))

kaartmaker()