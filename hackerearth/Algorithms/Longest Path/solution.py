"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque


def find_path(stack, adjacency):
    stack = deque(stack)
    max_node = -1
    max_depth = 0
    visited = set()
    while stack:
        node, depth = stack.pop()
        if depth > max_depth:
            max_depth = depth
            max_node = node
        if node not in visited:
            visited.add(node)
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))
    return max_node, max_depth


n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
edges = defaultdict(list)
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().strip().split())
    if not a[u] % k and not a[v] % k:
        edges[u].append(v)
        edges[v].append(u)
if not len(edges):
    print(0)
else:
    longest_node, _ = find_path([(i, 0) for i, v in enumerate(a) if not v % k], edges)
    _, longest_path = find_path([(longest_node, 0)], edges)
    print(longest_path)
