"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict
from collections import deque


def total_connected(adjacency, nodes, start, distance):
    visited = [False] * nodes
    visited[start - 1] = True
    cur_lvl = 0
    queue = deque()
    queue.append(start)
    level = {start: 0}
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if not visited[v - 1]:
                visited[v - 1] = True
                level[v] = level[u] + 1
                cur_lvl = level[v]
                queue.append(v)
        if cur_lvl > distance:
            break
    count = 0
    for dist in level.values():
        if dist == distance:
            count += 1
    return count


n, e = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(e):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
m = int(input())
for _ in range(m):
    src, t = list(map(int, input().split()))
    print(total_connected(graph, n, src, t))
