"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque
from sys import stdin


def find(x, p):
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(x, y, p, r):
    px = find(x, p)
    py = find(y, p)
    if r[px] < r[py]:
        p[px] = py
    elif r[px] > r[py]:
        p[py] = px
    else:
        p[py] = px
        r[px] += 1


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    graph = []
    for _ in range(m):
        a, b, c = map(int, stdin.readline().strip().split())
        graph.append((a - 1, b - 1, c))
    graph.sort(key=lambda x: x[-1])
    parents = [i for i in range(n)]
    ranks = [0] * n
    idx = 0
    stack = deque(graph.copy())
    weights = []
    while stack:
        a, b, c = stack.pop()
        pa = find(a, parents)
        pb = find(b, parents)
        if pa != pb:
            idx += 1
            weights.append(c)
            union(pa, pb, parents, ranks)
        if idx == n - 1:
            break
    print(sum(weights))
