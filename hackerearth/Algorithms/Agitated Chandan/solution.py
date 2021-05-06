"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque, defaultdict


def pay(adj, ln):
    visited = [False] * ln
    distances = [0] * ln
    max_distance = 0
    farthest_vertex = 0
    visited[0] = True
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                distances[v] = distances[u] + w
                if distances[v] >= max_distance:
                    max_distance = distances[v]
                    farthest_vertex = v
    visited = [False] * ln
    distances = [0] * ln
    max_distance = 0
    visited[farthest_vertex] = True
    queue.append(farthest_vertex)
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                distances[v] = distances[u] + w
                if distances[v] > max_distance:
                    max_distance = distances[v]
    if max_distance > 10000:
        cost = 10000
    elif max_distance > 1000:
        cost = 1000
    elif max_distance > 100:
        cost = 100
    else:
        cost = 0
    return cost, max_distance


t = int(input())
for _ in range(t):
    n = int(input())
    adjacency = defaultdict(list)
    for _ in range(n - 1):
        a, b, weight = map(int, input().strip().split())
        a -= 1
        b -= 1
        adjacency[a].append((b, weight))
        adjacency[b].append((a, weight))
    print(*pay(adjacency, n))
