weekendritJa = ["ja", "Ja", "yes", "Yes", "j", "J", "Y", "y"]
leeftijdKind = 12
leeftijdOud = 65
langeRit = 50
korteRit = 20
testGetallen = ((11, 12, 64, 65), ("Y" "N"), (70, 30, -1))

def standaardtarief(afstandKM):
    if afstandKM > langeRit:
        res = 15 + ((afstandKM - langeRit) * 0.60)
    if afstandKM >= 0:
        res = afstandKM * 0.80
    else:
        res = 0
    return res

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardPrijs = standaardtarief(afstandKM)
    if leeftijd < leeftijdKind or leeftijd > leeftijdOud:
        res = standaardPrijs * 0.70
        if weekendrit in weekendritJa:
            res = standaardPrijs * 0.65
    elif weekendrit in weekendritJa:
        res = standaardPrijs * 0.60
    else:
        res = standaardPrijs
    return res

while True:
    try:
        afstandKM = int(input("Hoeveel KM gaat u reizen?: "))
        break
    except ValueError:
        print("Voer het aantal KM in cijfers in.")
while True:
    try:
        leeftijd = int(input("Wat is jou leeftijd?: "))
        break
    except ValueError:  
        print("Voer je leeftijd in jaren in.")
weekendrit = str(input("Gaat u in het weekend reizen?: "))
line = "De kosten van uw rid word {:.2f} euro, nog een fijne reis toegewenst!".format(ritprijs(leeftijd,weekendrit,afstandKM))
print(line)

for i in range(0, 24, 1):
    print("leeftijd = {} , weekendrit = {} aantalkm = {} prijs = {:.2f}".format(testGetallen[0][i%4], testGetallen[1][i%2], testGetallen[2][i%3], ritprijs(testGetallen[0][i%4], testGetallen[1][i%2], testGetallen[2][i%3])))