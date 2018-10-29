import xmltodict

def lezer():
    artiekelen = []
    with open('artiekelennn.xml', 'r') as myXMLFile:
        doc = xmltodict.parse(myXMLFile.read())
        for artikel in doc['artikelen']['artikel']:
            artiekelen.append(artikel['naam'])
        print(artiekelen)

lezer()

