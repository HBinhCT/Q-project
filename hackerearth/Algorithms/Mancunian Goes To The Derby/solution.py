"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def bfs(adj, start, size):
    res = []
    queue = deque([(start, 0), (start, 1)])
    visited = set()
    while queue:
        u, w = queue.popleft()
        if u == size:
            res.append(w)
        else:
            visited.add((u, w & 1))
            for v in adj[w & 1][u]:
                if (v, (w + 1) & 1) not in visited:
                    queue.append((v, w + 1))
            for v in adj[(w + 1) & 1][u]:
                if (v, (w + 2) & 1) not in visited:
                    queue.append((v, w + 2))
    return min(res) if res else float('inf')


n, e, q = map(int, input().strip().split())
road = [defaultdict(list), defaultdict(list)]
for _ in range(e):
    a, b = map(int, input().strip().split())
    road[0][a].append(b)
    road[1][b].append(a)
time = bfs(road, 1, n)
for _ in range(q):
    print('GGMU' if int(input()) >= time else 'FML')
