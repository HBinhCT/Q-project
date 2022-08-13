from collections import defaultdict
from heapq import heapify, heappush, heappop
from sys import stdin

from numpy import array, argpartition, full


def dijkstra(start, size, adjacency, distances):
    visited = [False] * (1 + size)
    distances[start][start] = 0
    heap = [(0, start)]
    heapify(heap)
    while heap:
        distance, node = heappop(heap)
        if not visited[node]:
            visited[node] = True
            for weight, neighbor in adjacency[node]:
                if not visited[neighbor]:
                    new_weight = distance + weight
                    if distances[start][neighbor] > new_weight:
                        distances[start][neighbor] = new_weight
                        heappush(heap, (new_weight, neighbor))


n, m = map(int, stdin.readline().strip().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, stdin.readline().strip().split())
    if a != b:
        graph[a].append((c, b))
        graph[b].append((c, a))
dists = full((n + 1, n + 1), 9999999999, dtype=int)
for i in range(1, n + 1):
    dijkstra(i, n, graph, dists)
q = int(stdin.readline())
for _ in range(q):
    u, l, r, k = map(int, stdin.readline().strip().split())
    x_distances = array((dists[u][l:r + 1]).copy())
    k_distances = argpartition(x_distances, k - 1)
    print(x_distances[k_distances[:k]][-1])
