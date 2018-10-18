def menu():
    while True:
        while True:
            try:
                keuze = int(input('\n1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug\n5: Ik wil stoppen \nVoer hier je keuze in: '))
            except ValueError:
                print("Voer een geldig getal in")
            else:
                break
        if keuze == 1:
            toon_aantal_kluizen_vrij()
        elif keuze == 2:
            nieuwe_kluis()
        elif keuze == 3:
            kluis_openen()
        elif keuze == 4:
            kluis_teruggeven()
        elif keuze == 5:
            print('Bedankt voor het gebruik maken van mijn programma')
            break

def toon_aantal_kluizen_vrij():
    f = open('kluizen.txt', 'r')
    content = f.readlines()
    f.close()
    aantalBezet = 0
    for item in content:
        if '\n' in item:
            aantalBezet = aantalBezet + 1
    aantalVrij = 12 - aantalBezetx
    print('Er zijn {} kluizen vrij'.format(aantalVrij))

def nieuwe_kluis():
    f = open('kluizen.txt', 'r')
    content = f.readlines()
    f.close()
    vrijeKluis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for line in content:
        var = line.split(';')
        if var[0] in vrijeKluis:
            vrijeKluis.remove(var[0])
    if 12 >= len(vrijeKluis) and len(vrijeKluis) > 0:
        print('Je kluisnummer is {}'.format(vrijeKluis[0]))
        while True:
            invoerCode = str(input('Voer hier je code van minimaal 4 karakters in: '))
            if 4 > len(invoerCode):
                print("Voer minimaal vier karakters in!")
            else:
                print('U heeft een nieuwe kluis gekregen')
                break
        bestand = open('kluizen.txt', 'a')
        bestand.write('{};{}\n'.format(vrijeKluis[0], invoerCode))
        bestand.close()
    else:
        print("Alle kluizen zijn bezet")

def kluis_openen():
    f = open('kluizen.txt', 'r')
    content = f.readlines()
    f.close()
    wachtwoordGoed = 0
    while True:
        try:
            kluisnummer = int(input("Wat is jou kluisnummer?: "))
        except ValueError:
            print("Voer een geldig getal in")
        else:
            break
    codeKluisnummer = str(input('Voer je code in: '))
    for line in content:
        if (str(kluisnummer) + ';' + str(codeKluisnummer) + '\n') == line:
            wachtwoordGoed = 1
    if wachtwoordGoed == 1:
        print('De kluis is geopend')
    else:
        print('Je hebt het verkeerde combinatie ingevoerd')

def kluis_teruggeven():
    f = open('kluizen.txt', 'r')
    content = f.readlines()
    f.close()
    wachtwoordGoed = 1
    while True:
        try:
            kluisnummer = int(input("Je gaat je kluis teruggeven, wat is jou kluisnummer?: "))
        except ValueError:
            print("Voer een geldig getal in")
        else:
            break
    codeKluisnummer = str(input('Voer je code in: '))
    bestand = open('kluizen.txt', 'w')
    goedGegaan = 0
    for line in content:
        if (str(kluisnummer) + ';' + str(codeKluisnummer) + '\n') != line:
            bestand.write(line)
        if (str(kluisnummer) + ';' + str(codeKluisnummer) + '\n') == line:
            goedGegaan = 1
    if goedGegaan == 0:
        print('Je hebt het verkeerde combinatie ingevoerd')
    elif goedGegaan == 1:
        print('Je hebt je kluis succesvol teruggegeven')
    bestand.close()

menu()