from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    vals = list(map(int, input().strip().split()))
    res = 1
    for i in vals:
        res = res * i // gcd(res, i)
    print(res)
