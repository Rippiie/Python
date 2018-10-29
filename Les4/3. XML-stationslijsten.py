import xmltodict

def processXML(filename):
    with open(filename, 'r') as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary



