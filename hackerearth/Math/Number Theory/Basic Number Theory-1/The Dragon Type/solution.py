from collections import defaultdict
from sys import stdin

n, p = map(int, stdin.readline().strip().split())
h = list(map(int, stdin.readline().strip().split()))
for line in stdin.readlines():
    for i in map(int, line.strip().split()):
        h.append(i)
counter = defaultdict(int)
for i in h:
    counter[i % p] += 1
max_size = 0
for i in range(2, p - 1):
    j = pow(i, p - 2, p)
    if i < j:
        max_size += max(counter[i], counter[j])
print(max_size + counter[0])
