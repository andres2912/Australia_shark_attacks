import csv

file = "global-shark-attack.csv"

def read(file):
    with open (file, 'r', encoding='utf-8') as csv_read:
        reader = csv.reader(csv_read, delimiter=';')
        header = next(reader)
        print(list(reader))
      

read(file)