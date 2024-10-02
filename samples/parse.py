import csv

print('[', end='')

with open('samples\\data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i, row in enumerate(csv_reader):
        if i!=0 and row[0] == "b'F'" and i % 4 == 0:
            print(row[4], end=', ')

print(']')
