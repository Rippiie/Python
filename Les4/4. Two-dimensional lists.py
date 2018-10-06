studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    res = 0
    loopCount = 0
    antw = []
    for row in studentencijfers:
       for item in row:
           loopCount = loopCount + 1
           res = res + item
           gemiddelde = res / loopCount
       antw.append(gemiddelde)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
   som = 0
   antw = 0
   loopCount = 0
   for row in studentencijfers:
       for item in row:
           som = som + item
           loopCount = loopCount + 1
       totaal = antw + som
   loopCount = loopCount + 1
   antw = totaal / loopCount
   return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))