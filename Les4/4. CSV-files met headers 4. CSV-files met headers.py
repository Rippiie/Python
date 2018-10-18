import csv

def inlezen():
    with open('newfile.csv', 'r') as myCVSFile:
        reader = csv.reader(myCVSFile, delimiter=';')
        score = '0'
        for row in reader:
            if row[2] > score:
                score = row[2]
                naam = row[0]
                datum = row[1]
    print('De hoogste score is: {} op {} behaald door {}'.format(score, datum, naam))

