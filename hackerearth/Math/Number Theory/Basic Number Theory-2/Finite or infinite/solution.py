from math import gcd
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    s = list(map(int, stdin.readline().strip().split()))
    g = s[0]
    for i in range(1, n):
        g = gcd(g, s[i])
        if g == 1:
            print('FINITE')
            break
    else:
        print('INFINITE')
