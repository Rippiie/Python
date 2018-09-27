leeftijdMeerderjarig = 18
bezitPaspoort = ['Ja', 'ja', 'yes', 'Yes', 'y', 'Y', 'j', 'J',]
while True:
    try:
        leeftijd = int(input("Geef je leeftijd: "))
        break
    except ValueError:
        print("Voer een geldig getal in!")
NederlandsPaspoort = input('Ben je in bezit van een Nederlands passpoort?: ')
wilStemmen = input("Wil je graag stemmen?: ")
if leeftijd > leeftijdMeerderjarig and  NederlandsPaspoort in bezitPaspoort  and wilStemmen in bezitPaspoort:
    print('Gefeliciteerd, je mag stemmen en wil stemmen!')
else:
    print('Je mag niet stemmen ga maar weg nu!')