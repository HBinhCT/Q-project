"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from heapq import heappush, heappop
from sys import stdin


def floyd_warshall(adj):
    ln = len(adj)
    dist = [[float('inf')] * ln for _ in range(ln)]
    for c1 in range(ln):
        dist[c1][c1] = 0
        for c2, d in adj[c1]:
            dist[c1][c2] = d
    for z in range(ln):
        for x in range(ln):
            for y in range(ln):
                dist[x][y] = min(dist[x][y], dist[x][z] + dist[z][y])
    return dist


def kruskal(g, ln):
    def find(x, p):
        while x != p[x]:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def merge(x, y, p, r):
        px = find(x, p)
        py = find(y, p)
        if px != py:
            if r[px] == r[py]:
                p[py] = px
                r[px] += 1
            elif r[px] > r[py]:
                p[py] = px
            else:
                p[px] = py

    parent = [i for i in range(ln)]
    rank = [0] * ln
    heap = []
    for d, u, v in g:
        heappush(heap, (d, u, v))
    res = 0
    while heap:
        d, u, v = heappop(heap)
        if find(u, parent) != find(v, parent):
            merge(u, v, parent, rank)
            res += d
    return res


t = int(stdin.readline())
for _ in range(t):
    n, m, k = map(int, stdin.readline().strip().split())
    roads = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, stdin.readline().strip().split())
        a -= 1
        b -= 1
        roads[a].append((b, c))
        roads[b].append((a, c))
    dist = floyd_warshall(roads)
    edges = []
    for i in range(k):
        for j in range(i + 1, k):
            edges.append((dist[i][j], i, j))
    print(kruskal(edges, k))
