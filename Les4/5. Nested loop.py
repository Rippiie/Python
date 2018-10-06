def nesting():
    for row in range(1,11,1):
        for item in range(1,11,1):
            uitkomst = row * item
            print('{} x {} = {}'.format(row, item, uitkomst))

nesting()