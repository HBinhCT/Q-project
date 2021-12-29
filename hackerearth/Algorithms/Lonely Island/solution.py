"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque
from sys import stdin

limit = 1e-9


def topological_sort(root, size, adj, ins, outs, ways):
    queue = deque([])
    for i in range(1, size + 1):
        if ins[i] == 0:
            queue.append(i)
    ways[root] = 1
    while queue:
        node = queue.popleft()
        for neighbour in adj[node]:
            ways[neighbour] += ways[node] / outs[node]
            ins[neighbour] -= 1
            if ins[neighbour] == 0:
                queue.append(neighbour)


n, m, r = map(int, stdin.readline().strip().split())
islands = defaultdict(list)
in_degree = [0] * (n + 1)
out_degree = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, stdin.readline().strip().split())
    islands[u].append(v)
    in_degree[v] += 1
    out_degree[u] += 1
res = [0] * (n + 1)
topological_sort(r, n, islands, in_degree, out_degree, res)
mx = -1
for i in range(1, n + 1):
    if out_degree[i] == 0:
        mx = max(mx, res[i])
ans = []
for i in range(1, n + 1):
    if out_degree[i] == 0 and abs(res[i] - mx) <= limit:
        ans.append(i)
print(*ans)
