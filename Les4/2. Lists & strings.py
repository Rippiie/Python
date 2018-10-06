def listmaker():
    goedeLijst = []
    lijst = eval(input("Geef lijst met minimaal 10 strings: "))
    for i in lijst:
        if len(i) == 4:
            goedeLijst.append(i)
    print("De nieuw-gemaakte lijst met alle vier-letter strings is:\n{}".format(goedeLijst))

listmaker()