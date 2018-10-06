def gemiddelde(zin):
    lengteTotaal = 0
    var = zin.split()
    loop = 1
    for i in var:
        lengteWoord = len(var[loop - 1])
        lengteTotaal = lengteTotaal + lengteWoord
        lengteGemiddeld = (lengteTotaal / loop)
        loop = loop + 1
    print(lengteGemiddeld)

gemiddelde(str(input("Voer hier een zin in: ")))