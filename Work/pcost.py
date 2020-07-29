# pcost.py
#
# Exercise 1.27
# import os

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
total = 0
for line in f:
    row = line.split(',')
    total = total + int(row[1]) * float(row[2].strip())
print(f'Total cost {total:0.2f}')
f.close()
