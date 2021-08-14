"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque

n = int(input())
edges = defaultdict(list)
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().strip().split())
    edges[u].append(v)
    edges[v].append(u)
visited = [False] * n
visited[0] = True
ans = 0
queue = deque([(0, 0)])
while queue:
    curr, count = queue.popleft()
    ans += count
    for vertex in edges[curr]:
        if not visited[vertex]:
            visited[vertex] = True
            queue.append((vertex, count + 1))
print(ans + n)
