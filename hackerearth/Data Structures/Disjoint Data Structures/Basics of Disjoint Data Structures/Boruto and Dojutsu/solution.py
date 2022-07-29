from collections import defaultdict
from sys import stdin


def find(a, parents):
    while a != parents[a]:
        parents[a] = parents[parents[a]]
        a = parents[a]
    return a


def union(a, b, parents, ranks, adj):
    pa = find(a, parents)
    pb = find(b, parents)
    if ranks[pa] > ranks[pb]:
        pa, pb = pb, pa
    for i in adj[pa]:
        adj[pb].add(i)
    parents[pa] = pb
    ranks[pb] += ranks[pa]


n, m, q = map(int, stdin.readline().strip().split())
colors = list(map(int, stdin.readline().strip().split()))
connection = []
for _ in range(m):
    u, v = map(int, stdin.readline().strip().split())
    u -= 1
    v -= 1
    connection.append((u, v))
queries = []
deleted = defaultdict(bool)
for _ in range(q):
    p, xy = map(int, stdin.readline().strip().split())
    xy -= 1
    if p == 1:
        u, v = connection[xy]
        deleted[(u, v)] = True
    queries.append((p, xy))
graph = [{i} for i in colors]
roots = list(range(n))
sizes = [1] * n
for u, v in connection:
    if not deleted[(u, v)]:
        union(u, v, roots, sizes, graph)
res = []
queries.reverse()
for p, xy in queries:
    if p == 1:
        u, v = connection[xy]
        union(u, v, roots, sizes, graph)
    else:
        p = find(xy, roots)
        res.append(len(graph[p]))
res.reverse()
for i in res:
    print(i)
