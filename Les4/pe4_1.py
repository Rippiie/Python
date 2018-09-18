name = input("Wat is jou voornaam: ")
age = int(input("Wat is jou leeftijd?: "))
leeftijdVorigJaar ="Beste " + str(name) + ", jouw leeftijg vorig jaar was " + str(age - 1) + ", gefeliciteerd!"
bye = "Tot ziens en bedankt voor het gebruik maken van mijn programma!"
print(leeftijdVorigJaar)
if age >= 18:
    print('Party time :)')
else:
    print(" Jammer man, nix18 ")
print(bye)