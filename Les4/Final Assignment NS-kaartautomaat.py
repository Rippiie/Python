def inlezen_beginstation(stations):
    while True:
        invoer = str(input('Wat is je beginstation?: '))
        if invoer in stations:
            return invoer
        else:
            print('Deze trein komt niet in {}.'.format(invoer))

def inlezen_eindstation(stations, beginstation):
    while True:
        invoer = str(input('Wat is je eindstation?: '))
        if invoer in stations and stations.index(invoer) > stations.index(beginstation):
            return invoer
        else:
            print('Deze trein komt niet in {}.'.format(invoer))

def omroepen_reis(stations, beginstation, eindstation):
    beginstationRank = stations.index(beginstation) + 1
    eindstationRank = stations.index(eindstation) + 1
    afstandStations = eindstationRank - beginstationRank
    prijs = afstandStations * 5
    print('Het beginstation {} is het {}e station in het traject'.format(beginstation, beginstationRank))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, eindstationRank))
    print('De afstand bedraag {} station(s)'.format(afstandStations))
    print('De prijs van het kaartje is {} euro'.format(prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for i in range(beginstationRank, (eindstationRank - 1), 1):
        print(' - {}'.format(stations[i]))
    print('Je stapt uit in: {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
