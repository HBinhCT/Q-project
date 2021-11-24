"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque, defaultdict


def compute(adjacency, source, target):
    visited = {source: {0: 0}}
    queue = deque([(source, 0, 0)])
    min_time = float('inf')
    while queue:
        curr, stamina, time = queue.popleft()
        if curr == target:
            min_time = min(min_time, time)
            continue
        elif time >= min_time:
            continue
        for u, v, w in adjacency[curr]:
            if u == curr:
                rejected = False
                for vu, vv in visited[u].items():
                    if vu >= v and vv <= time + w:
                        rejected = True
                        break
                if not rejected:
                    queue.append((u, v, time + w))
                    visited[u][v] = time + w
            else:
                rejected = False
                if u in visited:
                    for vu, vv in visited[u].items():
                        if vu >= stamina - v and vv <= time:
                            rejected = True
                            break
                if not rejected and stamina >= v:
                    queue.append((u, stamina - v, time))
                    if u in visited:
                        visited[u][stamina - v] = time
                    else:
                        visited[u] = {stamina - v: time}
    if min_time == float('inf'):
        return -1
    else:
        return min_time


n, m, a, b = map(int, input().strip().split())
trans = defaultdict(list)
for _ in range(m):
    x, y, z = map(int, input().strip().split())
    trans[x].append((y, z, 0))
    trans[y].append((x, z, 0))
for i in range(1, n + 1):
    c, h = map(int, input().strip().split())
    trans[i].append((i, c, h))
print(compute(trans, a, b))
