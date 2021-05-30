import csv

with open("pokemon.csv", 'r') as c:
    rd = csv.reader(c)
    for line in rd:
        print(line)