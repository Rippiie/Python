def programma():
    while True:
        invoer = str(input('Geef een string van vier letters:: '))
        if len(invoer) != 4:
            print('{} heeft {} letters'.format(invoer, len(invoer)))
        else:
            print('Inlezen van correcte string: {} is geslaagd'.format(invoer))
            break

programma()