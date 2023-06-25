from collections import defaultdict

n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
connected = defaultdict(int)
for i, v in enumerate(a):
    connected[v] = max(connected[v], b[i])
for i in a:
    print(connected[i], end=' ')
