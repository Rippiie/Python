maxAantalKlzuien = 12

info = open('kluizen.txt')
count = 0
for line in info:
    count = count + 1
info.close()


def toNumbers(list):
    count =0
    for num in list:
        number = ''
        for char in num:
            if char.isdigit() == True:
                number = number + char
        list[count] = int(number)
        count = count + 1
    return list

def getTaken(list):
    taken = []
    info = open('kluizen.txt')
    for line in info:
        taken.append(line.split(';')[0])
    info.close()
    taken = toNumbers(taken)
    return taken

def getNumberAndCode(melding,choise):
    kluisNummer = int(input('Welk kluis nummer heb je? '))
    list = []
    taken = getTaken(list)
    if kluisNummer in taken:
        code = input('Wat is je kluiscode? ')

        info = open('kluizen.txt')
        for line in info:
            if (str(kluisNummer) + ';') in line:
                valid = False
                while not valid:
                    # print(code+'\n'+str(line[line.find(';')+1:]))
                    print(code.strip())
                    print(line.split(';')[1].strip())
                    if code.strip() == line.split(';')[1].strip():
                        print(melding)
                        valid = True
                    else:
                        print(type(code))
                        print(type(str(line[line.find(';') + 1:])))
                        code = input('je code is onjuist, probeer het opnieuw: ')
                if valid == True and choise == 4:
                    info.close()
                    infoo = open('kluizen.txt','a+')
                    for line in infoo:
                        if (str(kluisNummer) + ';') in line:
                            bab = ''
                            # line = ''
                    infoo.close()
        info.close()
    else:
        print('Kluisnummer bestaat niet')



choise = int(input('1: Ik wil weten hoeveel kluizen er nog vrij zijn \n'
               '2: Ik wil een nieuwe kluis \n'
               '3: Ik wil even iets uit mijn kluis halen \n'
               '4: Ik geef mijn kluis terug\n '))

if choise == 1:
    print('Er zijn nog {} kluizen vrij'.format(maxAantalKlzuien-count))

if choise == 2:
    if count < maxAantalKlzuien:
        valid = False
        while valid != True:
            code = input('Geef pincode voor de kluis: ')
            if len(code) >= 4:
                valid = True
        list = []
        taken = getTaken(list)
        nieuweKluis = 1
        for num in range(1, maxAantalKlzuien + 1):
            if num not in taken:
                nieuweKluis = num
        info = open('kluizen.txt', 'a+')
        info.write('\n{};{}'.format(nieuweKluis,code))
        info.close()
        print('Je nieuwe kluis is nummer: {} met code: {} '.format(nieuweKluis,code))

if choise == 3:
    getNumberAndCode('Je kluis is geopend!',choise)
if choise == 4:
    # getNumberAndCode('Je kluis is terug gegeven!',choise)
    bab = ''