def kaartmaker():
    infile = open('Kaartnummers.txt', 'r')
    content = infile.readlines()
    infile.close()
    for line in content:
        var = line.split(',')
        naam = var[1].strip()
        print('{} heeft kaartnummer : {}'.format(naam, var[0]))

kaartmaker()