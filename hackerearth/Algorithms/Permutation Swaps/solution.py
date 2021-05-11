"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def bfs(num, adj, mapping):
    queue = deque([num])
    visited = {num: True}
    mapping[num] = num
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in visited:
                visited[v] = True
                queue.append(v)
                mapping[v] = num


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    p = list(map(int, input().strip().split()))
    q = list(map(int, input().strip().split()))
    adjacency = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().strip().split())
        x -= 1
        y -= 1
        adjacency[p[x]].append(p[y])
        adjacency[p[y]].append(p[x])
    checks = {}
    for i in range(1, n + 1):
        if i not in checks:
            bfs(i, adjacency, checks)
    for i in range(n):
        if p[i] != q[i]:
            if checks[p[i]] != checks[q[i]]:
                print('NO')
                break
    else:
        print('YES')
