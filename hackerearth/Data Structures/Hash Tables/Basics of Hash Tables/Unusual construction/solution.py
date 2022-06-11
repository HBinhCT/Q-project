from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    roads = defaultdict(list)
    for _ in range(m):
        l, r, w = map(int, input().strip().split())
        roads[(l, r)].append(w)
    x = 0
    for k in roads:
        x = max(len(roads[k]), x)
    amount = 0
    for k in roads:
        if len(roads[k]) < x:
            amount += sum(roads[k])
    print(amount)
