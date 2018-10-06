# Brut Force problem

# You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
# How many ways can you make change for a $100 dollar bill?

import itertools as it

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

list(it.combinations(bills, 3))

makes_100 = set()
for n in range(len(bills)):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.add(combination)
print(len(makes_100))
