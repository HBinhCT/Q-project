"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().split())


def dijkstra(roads, source):
    visited = set()
    dist = {source: 0}
    heap = [[0, source]]
    while heap:
        d, u = heappop(heap)
        if u not in visited:
            visited.add(u)
            for v, w in roads[u].items():
                new_dist = d + w
                if v not in dist or new_dist < dist[v]:
                    dist[v] = new_dist
                    heappush(heap, [new_dist, v])
    return dist


roads_1 = defaultdict(lambda: defaultdict(lambda: float('inf')))
roads_2 = defaultdict(lambda: defaultdict(lambda: float('inf')))
for _ in range(m):
    a, b, c = map(int, input().split())
    roads_1[a][b] = min(roads_1[a][b], c)
    roads_2[b][a] = min(roads_2[b][a], c)
dist_0 = dijkstra(roads_1, 1)
dist_1 = dijkstra(roads_2, n)
min_cost = float('inf')
for city_a in roads_1:
    for city_b in roads_1[city_a]:
        if city_a in dist_0 and city_b in dist_1:
            cost = dist_0[city_a] + dist_1[city_b]
            min_cost = min(min_cost, cost)
print(min_cost)
