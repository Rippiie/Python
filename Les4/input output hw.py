earnings = int(input("Wat verdien je per uur?: "))
hours = int(input("Hoeveel uur heb je gewerkt?: "))
earningsTotal = earnings * hours
line = "{} uur werken levert {} Euro op".format(hours, earningsTotal)
print(line)