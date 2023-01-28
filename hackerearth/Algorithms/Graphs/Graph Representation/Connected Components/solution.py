from collections import defaultdict


def check(u, adj):
    x = u
    for v in adj[u]:
        y = v * v
        while x % y == 0:
            x /= y
    return x


t = int(input())
m = 200001
sieve = defaultdict(list)
for i in range(2, m):
    if not sieve[i]:
        for j in range(i + i, m, i):
            sieve[j].append(i)
counter = defaultdict(lambda: -1)
counter[0] = 0
counter[1] = 1
for i in range(2, m):
    counter[i] = counter[i - 1]
    if check(i, sieve) == i:
        counter[i] += 1
for _ in range(t):
    n = int(input())
    print(counter[n])
