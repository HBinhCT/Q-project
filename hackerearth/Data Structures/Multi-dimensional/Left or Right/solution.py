from bisect import bisect_left, bisect_right, insort
from collections import defaultdict
from sys import stdin

n, q = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
idxes = defaultdict(list)
for i, v in enumerate(a):
    insort(idxes[v], i)
for _ in range(q):
    y, z, d = stdin.readline().strip().split()
    y = int(y)
    z = int(z)
    if z not in idxes:
        print(-1)
    else:
        if d == 'L':
            if idxes[z][0] > y:
                print(y + n - idxes[z][-1])
            else:
                i = bisect_right(idxes[z], y) - 1
                print(y - idxes[z][i])
        else:
            if idxes[z][-1] < y:
                print(n - y + idxes[z][0])
            else:
                i = bisect_left(idxes[z], y)
                print(idxes[z][i] - y)
