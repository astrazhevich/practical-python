# pcost.py
#
# Exercise 1.27
# import os

import csv
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    total = 0
    line_num = 1
    for row in rows:
        # row = line.split(',')
        try: 
            total = total + int(row[1]) * float(row[2].strip())
        except ValueError:
            print(f"Warning: wrong values in line {line_num}!")
        line_num += 1
    return(total)
    f.close()

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
    
