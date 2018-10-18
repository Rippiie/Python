import datetime
import csv

bestand = 'inloggers.csv'
def schrijven():
    with open('newfile.csv', 'w', newline='') as myCVSFile:
        writer = csv.writer(myCVSFile, delimiter=';')
        writer.writerow(('datum', 'voorletters', 'achternaam', 'geboortedatum', "email"))
        while True:
            naam = input("Wat is je achternaam? ")
            if naam == 'einde':
                break
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            datum = datetime.datetime.now()
            writer.writerow((datum, voorl, naam, gbdatum, email))

programma()
#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file