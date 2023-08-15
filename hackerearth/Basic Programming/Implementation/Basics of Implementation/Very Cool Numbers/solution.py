from collections import Counter
from re import findall

t = int(input())
cases = []
x = 0
for _ in range(t):
    r, k = map(int, input().strip().split())
    cases.append((r, k))
    x = max(x, r)
cools = []
for i in range(x + 1):
    cools.append(len(findall("(?=101)", bin(i)[2:])))
cache = {}
for case in cases:
    if case in cache:
        print(cache[case])
        continue
    r, k = case
    counter = Counter(cools[: r + 1])
    occur = 0
    for i, v in counter.items():
        if i >= k:
            occur += v
    cache[(r, k)] = occur
    print(occur)
