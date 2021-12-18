"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def move(start, adj, stack=None):
    visited = defaultdict(bool)
    visited[start] = True
    queue = deque([start])
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    while queue:
        u = queue.popleft()
        if stack is not None:
            stack.add(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances


n, e, k = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
m1, m2 = map(int, input().strip().split())
reached = set()
dist1 = move(m1, graph, reached)
if m2 not in reached:
    print(0)
else:
    dist2 = move(m2, graph)
    ans = 0
    q = int(input())
    for _ in range(q):
        n1, n2 = map(int, input().strip().split())
        ans += (n1 in reached and n2 in reached and dist1[n1] <= k and dist2[n2] <= k)
    print(ans)
