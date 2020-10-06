import csv

name = input()
def fuck():
    pasta = csv.DictReader(open('pasta.csv', mode='r'))
    for row in pasta:
        print(row[name])

fuck()
fuck()
fuck()
fuck()