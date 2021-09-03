"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n = int(input())
    soldiers = list(map(int, input().strip().split()))
    commander = 0
    hierarchy = defaultdict(list)
    for i, v in enumerate(soldiers, start=1):
        if v == 0:
            commander = i
        else:
            hierarchy[v].append(i)
    q = int(input())
    message = defaultdict(set)
    queries = []
    for _ in range(q):
        x, y = map(int, input().strip().split())
        queries.append((x, y))
        message[x].add(y)
    ans = defaultdict(lambda: -1)
    stack = deque([commander])
    visited = [False] * (n + 1)
    dp = [0] * (n + 1)
    while stack:
        u = stack[-1]
        if visited[u]:
            stack.pop()
            for v in message[u]:
                if visited[v]:
                    ans[(u, v)] = dp[u] - dp[v] - 1
            visited[u] = False
        else:
            visited[u] = True
            for v in reversed(hierarchy[u]):
                dp[v] = dp[u] + 1
                stack.append(v)
    for x, y in queries:
        print(ans[(x, y)])
