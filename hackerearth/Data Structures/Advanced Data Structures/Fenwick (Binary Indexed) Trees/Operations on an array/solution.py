from bisect import bisect_left, insort_left
from sys import stdin

n, x = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
if len(a) != n:
    for _ in range(n - 1):
        a.append(int(stdin.readline()))
idxes = []
for i, v in enumerate(a, start=1):
    if v == x:
        idxes.append(i)
idxes.append(float('inf'))
q = int(stdin.readline())
for _ in range(q):
    type_query, *val_query = map(int, stdin.readline().strip().split())
    if type_query == 1:
        l, r, k = val_query
        i = bisect_left(idxes, l) + k - 1
        print(idxes[i] if i < len(idxes) and idxes[i] <= r else -1)
    elif type_query == 2:
        index, value = val_query
        if a[index - 1] == x and value != x:
            idxes.remove(index)
        elif a[index - 1] != x and value == x:
            insort_left(idxes, index)
        a[index - 1] = value
