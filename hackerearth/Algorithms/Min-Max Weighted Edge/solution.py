"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
import sys

sys.setrecursionlimit(2000)


def dfs(x, graph):
    d = set()
    height = []
    for i in graph[x]:
        res = dfs(i, graph)
        if res >= 0:
            d.add(res)
            if not x:
                height.append(res)
        else:
            return -1
    ln = len(d)
    if not ln:
        return 0
    if x:
        return list(d)[0] + 1 if ln == 1 else -1
    else:
        if ln == 1:
            return height[0] + 1
        elif ln == 2:
            height.sort(reverse=True)
            return height[0] + 1 if height[0] != height[1] else -1
        else:
            return -1


t = int(input())
for _ in range(t):
    n, s = map(int, input().strip().split())
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().strip().split())
        adj[u - 1].append(v - 1)
    print(s // (n - 1) + (s % (n - 1) > 0) if dfs(0, tuple(adj)) != -1 else 0)
