"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from heapq import heappush, heappop
from sys import stdin

INF = float('inf')


def dijkstra(adj, size, src, des, parent):
    dist = [INF] * (size + 1)
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        total, node = heappop(heap)
        if dist[node] >= total:
            if node == des:
                break
            for neighbor, distance in adj[node]:
                new_distance = dist[node] + distance
                if dist[neighbor] > new_distance:
                    dist[neighbor] = new_distance
                    heappush(heap, (dist[neighbor], neighbor))
                    parent[neighbor] = node
    return dist


def trail(x, y, parent):
    res = []
    while True:
        res.append(x)
        x = parent[x]
        if x == y:
            res.append(x)
            break
    res.reverse()
    return res


t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().strip().split())
    stations = [[] for i in range(n + 1)]
    for _ in range(k):
        a, b, d = map(int, stdin.readline().strip().split())
        stations[a].append((b, d))
        stations[b].append((a, d))
    a, b, c = map(int, stdin.readline().strip().split())
    parents = [0] * (n + 1)
    res1 = []
    res2 = []
    dist_start = dijkstra(stations, n, a, b, parents)
    if dist_start[b] != INF:
        res1 = trail(b, a, parents)
    dist_end = dijkstra(stations, n, b, c, parents)
    if dist_end[c] != INF:
        res2 = trail(c, b, parents)
    if dist_start[b] != INF and dist_end[c] != INF:
        print(dist_start[b] + dist_end[c])
        print(' '.join(str(i) for i in res1 + res2[1:]))
    else:
        print('No Train Found.')
