"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin


def dijkstra(start, adj):
    distances = {i: float('inf') for i in adj}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]
    while heap:
        total, node = heappop(heap)
        if node not in visited:
            visited.add(node)
            for neighbor, cost in adj[node]:
                new_cost = total + cost
                if distances[neighbor] > new_cost:
                    distances[neighbor] = new_cost
                    heappush(heap, (new_cost, neighbor))
    return distances


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    road = defaultdict(list)
    for _ in range(m):
        x, y, c = map(int, stdin.readline().strip().split())
        road[x].append((y, c))
        road[y].append((x, c))
    dist = dijkstra(1, road)
    q = int(stdin.readline())
    for _ in range(q):
        a, k = map(int, stdin.readline().strip().split())
        spend = dist[a] * 2
        if spend >= k:
            print(0)
        else:
            print(k - spend)
