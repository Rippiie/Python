testGetallen =  [ 4, 5, 3, -81 ]
def kwadraten_som(grondGetallen):
    res = 0
    for i in grondGetallen:
        if i > 0:
            res = res + (i * i)
    return res

print(kwadraten_som(testGetallen))