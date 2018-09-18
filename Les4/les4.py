while True:
    try:
        age =int(input("Wat is jou leeftijg?: "))
    except ValueError:
        print("Voer een geldig getal in")
    else:
        break
ageOud = 62
if age > ageOud:
    print("You can get Social Security benefits")
else:
    print("You are not old enough")
