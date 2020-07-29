# pcost.py
#
# Exercise 1.27
# import os

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f)
    total = 0
    line_num = 1
    for line in f:
        row = line.split(',')
        try: 
            total = total + int(row[1]) * float(row[2].strip())
        except ValueError:
            print(f"Warning: wrong values in line {line_num}!")
        line_num += 1
    return(total)
    f.close()

# cost = portfolio_cost('Data/portfolio.csv')
# print(f'Total cost {cost:0.2f}')
