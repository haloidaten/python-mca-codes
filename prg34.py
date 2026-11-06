import csv

f = open(r"C:\Users\USER\Documents\mca\python\s.csv", "r")

r = csv.reader(f)

for row in r:
    print(row)

f.close()