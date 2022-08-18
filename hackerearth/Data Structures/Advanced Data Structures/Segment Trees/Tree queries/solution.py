from collections import defaultdict
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    edges = defaultdict(list)
    for _ in range(n - 1):
        u, v = [int(i) - 1 for i in stdin.readline().strip().split()]
        edges[u].append(v)
        edges[v].append(u)
    dists = [float('inf')] * n
    queue = [0]
    i = 0
    while queue:
        new_queue = []
        for u in queue:
            dists[u] = i
            for v in edges[u]:
                if dists[v] == float('inf'):
                    new_queue.append(v)
        queue = new_queue
        i += 1
    longest_dists = [0] * i
    for i, v in enumerate(a):
        longest_dists[dists[i]] = max(longest_dists[dists[i]], v)
    longest_dist = max(longest_dists)
    q = int(stdin.readline())
    for _ in range(q):
        p, *query = map(int, stdin.readline().strip().split())
        if p == 1:
            u, x = query
            u -= 1
            a[u] += x
            longest_dists[dists[u]] = max(longest_dists[dists[u]], a[u])
            longest_dist = max(longest_dist, longest_dists[dists[u]])
        else:
            p = query[0]
            if p >= longest_dist:
                print(-1)
            else:
                print(next(i for i, v in enumerate(longest_dists) if v > p))
