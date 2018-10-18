def ticker(fileName):
    f = open('ticker.txt', 'r')
    content = f.readlines()
    f.close()
    dict = {}
    for line in content:
        var = line.split(':')
        dict[var[0]] = var[1]
    return dict

def programm():
    dict = ticker(ticker)
    bedrijfNaam = str(input('Enter company name: '))
    for x, y in dict.items():
        if x == bedrijfNaam:
            res = y
    print('Ticker symbol: {}'.format(res))
    tickerNaam = str(input('Enter Ticker symbol:'))
    for x, y in dict.items():
        if y == tickerNaam:
            res = x
    print('Company name: {}'.format(res))

programm()