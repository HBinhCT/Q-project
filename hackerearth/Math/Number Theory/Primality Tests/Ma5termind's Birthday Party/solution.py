from itertools import accumulate

t = int(input())
groups = []
n = 0
for _ in range(t):
    l, r = map(int, input().strip().split())
    groups.append((l, r))
    n = max(n, r)
n += 1
primes = [False] * 2 + [True] * (n - 2)
i = 2
while i * i < n:
    if primes[i]:
        for j in range(i * i, n, i):
            primes[j] = False
    i += 1
primes[4] = True
counts = list(accumulate(primes))
for l, r in groups:
    print((r - l + 1) - (counts[r] - counts[l - 1]))
