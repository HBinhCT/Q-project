"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from heapq import heappop, heappush

n, m = map(int, input().strip().split())
g = defaultdict(list)
for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().strip().split())
    g[u].append(v)
    g[v].append(u)
a = list(map(int, input().strip().split()))
start, end = map(lambda x: int(x) - 1, input().strip().split())
heap = [(0, start)]
visited = [False] * n
while heap:
    path, u = heappop(heap)
    if u == end:
        print(path)
        break
    if not visited[u]:
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                heappush(heap, (max(path, abs(a[v] - a[u])), v))
