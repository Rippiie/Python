leeftijdKind = 12
leeftijdOud = 65
langeRit = 50
korteRit = 20
testGetallen = ((11, 12, 64, 65), ("Y" "N"), (70, 30, -1))
vastTariefLangeRit = 15
extraKostenKMLangeRit = 0.60
prijsKMKorteRit = 0.80
heeftRechtOpLeeftijdsKorting = False
weekendrit = False
afstandKM = int()
leeftijd = ''

def standaardtarief(afstandKM):
    if afstandKM > langeRit:
        res = vastTariefLangeRit + ((afstandKM - langeRit) * extraKostenKMLangeRit)
    if afstandKM >= 0:
        res = afstandKM * prijsKMKorteRit
    else:
        res = 0
    return res

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardPrijs = standaardtarief(afstandKM)
    if heeftRechtOpLeeftijdsKorting == True:
        res = standaardPrijs * 0.70
        if weekendrit == True:
            res = standaardPrijs * 0.65
    elif weekendrit == True:
        res = standaardPrijs * 0.60
    else:
        res = standaardPrijs
    return res

def getGebruikersInput(afstandKM, leeftijd, weekendrit, heeftRechtOpLeeftijdsKorting):
    while True:
        try:
            afstandKM = int(input("Hoeveel KM gaat u reizen?: "))
            leeftijd = int(input("Wat is jou leeftijd?: "))
            weekendrit = str(input("Gaat u in het weekend reizen?: "))
            weekendrit = weekendrit[0]
            weekendrit.upper()
            if weekendrit == 'J' or weekendrit == 'Y':
                weekendrit = True
            if leeftijd < leeftijdKind or leeftijd > leeftijdOud:
                heeftRechtOpLeeftijdsKorting = True
            break
        except ValueError:
            print("Voer eene geldige invoer in")

getGebruikersInput(afstandKM, leeftijd, weekendrit, heeftRechtOpLeeftijdsKorting)
standaardtarief(afstandKM)
ritprijs(leeftijd, weekendrit, afstandKM)
line = "De kosten van uw rid word {:.2f} euro, nog een fijne reis toegewenst!".format(ritprijs(leeftijd,weekendrit,afstandKM))
print(line)

for i in range(0, 24, 1):
    print("leeftijd = {} , weekendrit = {} aantalkm = {} prijs = {:.2f}".format(testGetallen[0][i%4], testGetallen[1][i%2], testGetallen[2][i%3], ritprijs(testGetallen[0][i%4], testGetallen[1][i%2], testGetallen[2][i%3])))