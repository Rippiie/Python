invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
def programma():
    lijstUnsort = invoer.split('-')
    lijstUnsort.sort()
    lijst = list(map(int, lijstUnsort))
    grootsteWaarden = max(lijst)
    kleinsteWaarden = min(lijst)
    aantalGetallen = len(lijst)
    somGetallen = sum(lijst)
    gemiddelde = sum(lijst) / len(lijst)
    print("Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal: {}\nAantal getallen: {} en Som van getallen: {}\nGemiddelde: {}".format(lijst, grootsteWaarden, kleinsteWaarden, aantalGetallen,somGetallen, gemiddelde ))

programma()