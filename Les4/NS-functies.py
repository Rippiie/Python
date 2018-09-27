weekenritJa = ("ja", "Ja", "yes", "Yes", "j", "J", "Y", "y")
def standaardtarief(afstandKM):
    if afstandKM >= 50:
        res = 15 + (afstandKM - 50) * 0.60
    if afstandKM > 0:
        res = afstandKM * 0.80
    if afstandKM < 0:
        res = 0
    return res
def ritprijs(leeftijd, weekendrit, afstandKM):
    res = standaardtarief(afstandKM)
    if leeftijd >= 12 and leeftijd > 65:
        res = int(standaardtarief(afstandKM)) * 0.70
    if leeftijd >= 12 and leeftijd > 65 and weekendrit == "ja":
        res = int(standaardtarief(afstandKM)) * 0.65
    if weekendrit in weekenritJa:
        res = int(standaardtarief(afstandKM)) * 0.60
    else:
        res = int(standaardtarief(afstandKM))
    return res
while True:
    try:
        afstandKM = int(input("Hoeveel KM gaat u reizen?: "))
        break
    except ValueError:
        print("Voer het aantal KM in cijfers in.")
while True:
    try:
        leeftijd = int(input("Wat is jou leeftjid?: "))
        break
    except ValueError:
        print("Voer je leeftijd in jaren in.")
weekendrit = str(input("Gaat u in het weekend reizen?: "))
line = "De kosten van uw rid word {:.2f} euro, nog een fijne reis toegewenst!".format(ritprijs(leeftijd,weekendrit,afstandKM))
print(line)