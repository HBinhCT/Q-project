"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from heapq import heappush, heappop
from sys import stdin


def dijkstra(adj, values, start):
    dist = [(float('inf')) for _ in range(len(adj))]
    dist[start] = values[start]
    heap = [(values[start], start)]
    while heap:
        val, node = heappop(heap)
        if val <= dist[node]:
            for neighbor in adj[node]:
                new_val = max(dist[node], values[neighbor])
                if dist[neighbor] > new_val:
                    dist[neighbor] = new_val
                    heappush(heap, (dist[neighbor], neighbor))
    return dist


t = int(stdin.readline())
for _ in range(t):
    n, m, s = map(int, stdin.readline().strip().split())
    sweets = [0] + list(map(int, stdin.readline().strip().split()))
    roads = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, stdin.readline().strip().split())
        roads[u].append(v)
    print(*dijkstra(roads, sweets, s)[1:])
