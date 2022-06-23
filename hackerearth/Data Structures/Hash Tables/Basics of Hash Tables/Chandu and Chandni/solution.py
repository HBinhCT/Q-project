from collections import defaultdict
from math import ceil

t = int(input())
n = 0
positions = []
for _ in range(t):
    a, b = map(int, input().strip().split())
    positions.append((a, b))
    n = max(n, a)
p = (1 + 5 ** .5) / 2
playing = defaultdict(lambda: - 1)
for i in range(ceil(n / p) + 1):
    playing[int(i * p)] = int(i * p * p)
for a, b in positions:
    print('Chandu' if playing[a] == b else 'Chandni')
