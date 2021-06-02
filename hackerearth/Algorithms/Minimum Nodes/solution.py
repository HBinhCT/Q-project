"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def find_path(start, least, vls, adjacency, visited):
    queue = deque()
    queue.append((vls[start], start, 1))
    while queue:
        val, node, dist = queue.popleft()
        if val >= least:
            return dist
        if not visited[node]:
            visited[node] = True
            for vertex in adjacency[node]:
                if not visited[vertex]:
                    queue.append((val + vls[vertex], vertex, dist + 1))
    return -1


n, q = map(int, input().strip().split())
values = list(map(int, input().strip().split()))
edges = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)
for _ in range(q):
    x, k = map(int, input().strip().split())
    print(find_path(x - 1, k, values, edges, [False] * n))
