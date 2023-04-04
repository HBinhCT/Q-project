from itertools import product
from math import prod

n = int(input())
count = 0
d = []
for i in range(2, 10):
    if not n % i:
        d.append(i)
for i in range(1, 7):
    for j in product(d, repeat=i):
        if prod(list(j)) == n:
            count += 1
print(count)
