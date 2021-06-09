"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def find_strength(nodes, adjacency):
    queue = deque([1])
    visited = [0] * nodes
    counter = [0] * nodes
    res = {}
    while queue:
        u = queue[-1]
        if not visited[u]:
            queue.extend(v for v in adjacency[u] if not visited[v])
            visited[u] = 1
        else:
            count = 1
            for v in adjacency[u]:
                if visited[v] == -1:
                    cv = counter[v]
                    res[(u, v)] = (nodes - cv) * cv
                    count += cv
            counter[u] = count
            visited[u] = -1
            queue.pop()
    return res


n = int(input())
m, _ = map(int, input().strip().split())
tree = defaultdict(set)
edges = []
for _ in range(n - 1):
    x, y = map(int, input().strip().split())
    x -= 1
    y -= 1
    tree[x].add(y)
    tree[y].add(x)
    edges.append((x, y))
strength = find_strength(n, tree)
for x, y in edges:
    if (x, y) in strength:
        print(strength[(x, y)])
    else:
        print(strength[(y, x)])
