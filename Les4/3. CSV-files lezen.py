import csv
import os

def schrijven():
    if os.path.isfile('./artiekelen.csv'):
        with open('artiekelen.csv', 'a', newline='') as myCVSFile:
            writer = csv.writer(myCVSFile, delimiter=';')
            while True:
                artiekelnmmr = int(input("Wat is het Artiekelnummer?: (stopcode is 999)"))
                if artiekelnmmr == 999:
                    break
                artiekelcode = str(input("Wat is de artiekelcode?: "))
                naamArtiekel = str(input("Wat is de naam van het artiekel?: "))
                voorraad = int(input("Wat is de voorraad?: "))
                prijs = float(input('Wat is de prijs?: '))
                writer.writerow((artiekelnmmr, artiekelcode, naamArtiekel, voorraad, prijs))
    else:
        with open('artiekelen.csv', 'w+', newline='') as myCVSFile:
            writer = csv.writer(myCVSFile, delimiter=';')
            writer.writerow(('Artiekelnummer', 'Artiekelcode', 'Naam', 'Voorraad', "Prijs"))
            while True:
                artiekelnmmr = int(input("Wat is het Artiekelnummer?: (stopcode is 999)"))
                if artiekelnmmr == 999:
                    break
                artiekelcode = str(input("Wat is de artiekelcode?: "))
                naamArtiekel = str(input("Wat is de naam van het artiekel?: "))
                voorraad = int(input("Wat is de voorraad?: "))
                prijs = float(input('Wat is de prijs?: '))
                writer.writerow((artiekelnmmr, artiekelcode, naamArtiekel, voorraad, prijs))

def inlezen():
    with open('artiekelen.csv', 'r') as myCVSFile:
        reader = csv.reader(myCVSFile, delimiter=';')
        next(reader)
        prijs = 0.0
        naamArtiekel = ''
        voorraad = 10000
        artiekelnummer = 0
        voorraadTotaal = 0
        for row in reader:
            if float(row[4]) > float(prijs):
                prijs = row[4]
                naamArtiekel = row[2]
            if int(row[3]) < int(voorraad):
                voorraad = row[3]
                artiekelnummer = row[0]
            voorraadTotaal += int(row[3])
    print('Het duurste artikel is {} en die kost {} Euro'.format(naamArtiekel, prijs))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(voorraad, artiekelnummer))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(voorraadTotaal))

#schrijven
#inlezen()