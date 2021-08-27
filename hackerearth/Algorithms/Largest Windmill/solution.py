"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque

n = int(input())
paths = defaultdict(set)
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().strip().split())
    paths[u].add(v)
    paths[v].add(u)
parents = [-1] * n
stack = deque([0])
vertexes = deque([])
lens = [len(paths[i]) for i in range(n)]
while stack:
    u = stack.popleft()
    vertexes.append(u)
    for v in paths[u]:
        stack.append(v)
        paths[v].remove(u)
        parents[v] = u
levels = [0] * n
while vertexes:
    u = vertexes.pop()
    lvl = 0
    for v in paths[u]:
        lvl = max(lvl, levels[v] + 1)
    levels[u] = lvl
result = -1
c = None
for i in range(n):
    if lens[i] >= 5:
        u = i
        lvl = levels[u]
        d = 1
        while parents[u] != -1:
            d += 1
            for v in paths[parents[u]]:
                if v != u:
                    lvl = max(lvl, levels[v] + d)
            u = parents[u]
        if lvl + lens[i] > result:
            result = lvl + lens[i]
            c = i
if result != -1:
    print(result, c + 1)
else:
    print(-1)
