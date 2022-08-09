from collections import defaultdict

n, m, k = map(int, input().strip().split())
a = [0] + list(map(int, input().strip().split()))
p = list(map(int, input().strip().split()))
connected = defaultdict(int)
counter = defaultdict(int)
connected[(1, a[2])] = 1
counter[2] = 1
pairs = 0
if a[1] == a[2]:
    pairs += 1
for i, j in enumerate(p, start=3):
    counter[i] = j
    pairs += a[i] == a[j]
    connected[(j, a[i])] += 1
for _ in range(m):
    x, y = map(int, input().strip().split())
    sub = connected[(x, a[x])]
    sub += a[counter[x]] == a[x]
    add = connected[(x, y)]
    add += a[counter[x]] == y
    pairs += add - sub
    connected[(counter[x], a[x])] -= 1
    connected[(counter[x], y)] += 1
    a[x] = y
    print(pairs)
