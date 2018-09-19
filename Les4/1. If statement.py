scoreGeslaagd = 15
while True:
    try:
        score =int(input("Wat is jou score?: "))
    except ValueError:
        print("Voer een geldig getal in")
    else:
        break
if score > scoreGeslaagd:
    print("Gefeliciteerd")
    print("Met een score van {} ben je geslaagd!".format(score))
else:
    print('Je bent niet geslaagd')