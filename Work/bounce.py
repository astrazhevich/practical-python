# bounce.py
#
# Exercise 1.5

h = 100
reduce_koef = 3 / 5

for i in range(10):
    h = h * reduce_koef
    print(round(h, 4))