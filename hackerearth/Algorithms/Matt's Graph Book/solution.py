"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys
from collections import defaultdict

sys.setrecursionlimit(100000)


def check(node, adjacency, seen):
    seen[node] = True
    for vertex in adjacency[node]:
        if not seen[vertex]:
            check(vertex, adjacency, seen)


n = int(input())
k = int(input())
edges = defaultdict(list)
for _ in range(k):
    a, b = list(map(int, input().strip().split()))
    edges[a].append(b)
    edges[b].append(a)
x = int(input())
count = 0
visited = defaultdict(bool)
visited[x] = True
for i in range(n):
    if not visited[i]:
        count += 1
        check(i, edges, visited)
print('Connected' if count == 1 else 'Not Connected')
