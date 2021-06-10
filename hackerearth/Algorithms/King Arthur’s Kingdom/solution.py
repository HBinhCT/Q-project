"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque

t = int(input())
for i in range(t):
    n, k = map(int, input().strip().split())
    values = list(map(int, input().strip().split()))
    edges = defaultdict(list)
    first = -1
    for j in range(n - 1):
        u, v = map(int, input().strip().split())
        if not j:
            first = u
        edges[u].append(v)
        edges[v].append(u)
    stack = deque(map(lambda x: (first, x), edges[first]))
    total = 1
    sub_trees = []
    visited = [first]
    while stack:
        parent, child = stack.pop()
        if child not in visited:
            visited.append(child)
            stack += list(map(lambda x: (child, x), edges[child]))
            count = 1 + (values[parent - 1] != values[child - 1])
            total += 1 + (count <= k)
            ln = len(sub_trees)
            sub_trees.append([parent, child])
            for j in range(ln):
                sub_tree = sub_trees[j]
                if parent in sub_tree:
                    new_tree = sub_tree + [child]
                    total += len(set(map(lambda x: values[x - 1], new_tree))) <= k
                    sub_trees.append(new_tree)
    print(f'Case {i + 1}: {total}')
