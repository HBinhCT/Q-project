from collections import defaultdict, deque
from math import gcd

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = [int(i) - 1 for i in input().strip().split()]
    graph[u].append(v)
    graph[v].append(u)
disc = [0] * n
low = [0] * n
counts = [1] * n
total = valid = 0
parents = [-1] * n
visited = {0}
stack = deque([0])
while stack:
    u = stack[-1]
    if not graph[u]:
        p = parents[u]
        if p != -1:
            counts[p] += counts[u]
            low[p] = min(low[p], low[u])
            if disc[p] < low[u]:
                total += 1
                if counts[u] % 2 == (n - counts[u]) % 2 == 0:
                    valid += 1
        stack.pop()
    else:
        v = graph[u].pop()
        if v not in visited:
            stack.append(v)
            count = len(visited)
            disc[v] = count
            low[v] = count
            parents[v] = u
            visited.add(v)
        elif v != parents[u]:
            low[u] = min(low[u], disc[v])
if total == 0:
    x = y = 0
else:
    mod = 1000000007


    def get_pow(a, b):
        res = 1
        while b:
            if b & 1:
                res = res * a % mod
            a = a * a % mod
            b >>= 1
        return res


    common = gcd(total, valid)
    total //= common
    valid //= common
    tot = get_pow(total, mod - 2)
    x = valid * tot % mod
    y = (total - valid) * tot % mod
print(x, y)
