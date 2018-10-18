def seizoen(maand):
    if 0 >= maand or maand >= 13:
        res = 'Voer een geldige maand in'
    elif maand >= 1 and maand <= 3:
        res = "het is winter"
    elif maand >= 4 and maand <= 6:
        res = 'het is lente'
    elif maand >= 7 and maand <= 9:
        res ='het is zomer'
    elif maand >= 10 and maand <= 12:
        res = 'het is zomer'
    return res

print(seizoen(1))
