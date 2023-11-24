from functools import reduce
from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    x = reduce(gcd, a)
    if 1 == x:
        print(0)
        continue
    for i in range(n - 1, -1, -1):
        if 1 == gcd(x, i + 1):
            print(n - i)
            break
        if n - i >= 3:
            print(3)
            break
    else:
        print(3)
