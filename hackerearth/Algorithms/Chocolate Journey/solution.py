"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from heapq import heappop, heappush
from sys import stdin

INF = float('inf')


def solve():
    def dijkstra(start, adj, size):
        dist = [INF] * (n + 1)
        visited = [False] * (size + 1)
        heap = [(0, start)]
        dist[start] = 0
        while heap:
            length, node = heappop(heap)
            if not visited[node]:
                visited[node] = True
                for next_length, next_node in adj[node]:
                    new_length = next_length + dist[node]
                    if dist[next_node] > new_length:
                        dist[next_node] = new_length
                        heappush(heap, (dist[next_node], next_node))
        return dist

    n, m, k, x = map(int, stdin.readline().strip().split())
    cities = list(map(int, stdin.readline().strip().split()))
    roads = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v, d = map(int, stdin.readline().split())
        roads[u].append((d, v))
        roads[v].append((d, u))
    a, b = map(int, stdin.readline().strip().split())
    dist_a = dijkstra(a, roads, n)
    dist_b = dijkstra(b, roads, n)
    time = INF
    for city in cities:
        if dist_b[city] <= x:
            time = min(time, dist_a[city] + dist_b[city])
    print(time if time != INF else -1)


solve()
