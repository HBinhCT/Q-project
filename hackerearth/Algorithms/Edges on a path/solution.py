"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def find_path(node, end, adj, size, visited=None, path=None, res=None):
    if visited is None:
        visited = [False] * (size + 1)
    if path is None:
        path = deque([])
    if res is None:
        res = []
    visited[node] = True
    path.append(node)
    if node == end:
        res.append(list(path))
    else:
        for neighbor in adj[node]:
            if not visited[neighbor]:
                find_path(neighbor, end, adj, size, visited, path, res)
    path.pop()
    visited[node] = False
    return res


n, m = map(int, input().strip().split())
a, b = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)
ans = find_path(a, b, graph, n)
if len(ans) == 1:
    print(len(ans[0]) - 1)
else:
    p = q = 0
    ln = min(len(ans[0]), len(ans[1]))
    for i in range(ln):
        p += ans[0][i] == ans[1][i]
    ans = [ans[0][::-1], ans[1][::-1]]
    for i in range(ln):
        q += ans[0][i] == ans[1][i]
    print(p + q - 2)
