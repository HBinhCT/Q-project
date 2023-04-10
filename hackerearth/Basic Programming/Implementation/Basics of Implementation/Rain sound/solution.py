from math import ceil, floor
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    l, r, s = map(int, stdin.readline().strip().split())
    x = ceil(l / s)
    y = floor(r / s)
    if s > r or x > y:
        print(-1, -1)
    else:
        print(x, y)
