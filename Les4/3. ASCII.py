def code(invoerstring):
    gecodeerd = str()
    for char in invoerstring:
        var = ord(char) + 3
        gecodeerd = gecodeerd + chr(var)
    return gecodeerd
print(code(invoerstring = 'RutteAlkmaarDen Helder'))