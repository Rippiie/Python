import random
def monopolyworp():
    getal1 = random.randrange(0, 7)
    getal2 = random.randrange(0, 7)
    getal3 = random.randrange(0, 7)
    getal4 = random.randrange(0, 7)
    som1 = getal1 + getal2
    som2 = getal3 + getal4
    if getal1 != getal2:
        print('{} + {} = {}'.format(getal1, getal2, som1))
    elif getal1 == getal2:
        print('{} + {} = {}(dubbel)'.format(getal1, getal2, som1))
        if getal3 != getal4:
            print('{} + {} = {}'.format(getal3, getal4, som2))
        elif getal3 == getal4:
            print('{} + {} = (direct naar gevangenis)'.format(getal3, getal4, som2))

monopolyworp()