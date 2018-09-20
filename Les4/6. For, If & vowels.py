s = "Guido van Rossum heeft programmeertaal Python bedacht."
medeklinkers = 'aeiou'
for char in s:
    if char in medeklinkers:
        print(char)