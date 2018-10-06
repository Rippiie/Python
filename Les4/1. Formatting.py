def convert(Celcius):
    res = (Celcius * 1.8) + 32
    return res

def table():
    print("{:7} {:7}".format("F", "C"))
    for i in range(-30, 40, 10):
        res = convert(i)
        print("{:5.1f} {:5.1f}".format(res, i))

print(table())