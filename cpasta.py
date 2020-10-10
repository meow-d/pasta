import csv

'''
name = input()
def fuck():
    pasta = csv.DictReader(open('pasta.csv', mode='r'))
    for row in pasta:
        print(row[name])
'''

def filterFunc(x):
    if x == "pastaName":
        return False
    else:
        return True

pasta = csv.DictReader(open('pasta.csv', mode='r'))
print('\n'.join(filter(filterFunc,pasta.fieldnames)))