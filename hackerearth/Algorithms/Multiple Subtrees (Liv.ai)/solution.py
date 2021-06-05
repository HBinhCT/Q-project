"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque, defaultdict

n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    u -= 1
    v -= 1
    tree[u].append(v)
    tree[v].append(u)
queue = deque([(0, i) for i in tree[0]])
subtrees = [0] * n
subtrees[0] = len(tree[0])
while queue:
    parent, node = queue.popleft()
    subtrees[node] = subtrees[parent] - 1 + len(tree[node]) - 1
    for child in tree[node]:
        if child != parent:
            queue.append((node, child))
q = int(input())
for _ in range(q):
    broken_node = int(input())
    print(subtrees[broken_node - 1])
