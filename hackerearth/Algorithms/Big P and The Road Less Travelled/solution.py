"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict, deque

n = int(input())
pairs = defaultdict(list)
while True:
    # input()
    x, y = map(int, input().strip().split())
    if (x, y) == (0, 0):
        break
    pairs[x].append(y)
dp = [0] * (n + 1)
dp[1] = 1
visited = [False] * (n + 1)
visited[1] = True
queue = deque([1])
while queue:
    checkpoint = queue.popleft()
    for i in pairs[checkpoint]:
        dp[i] += dp[checkpoint]
        if not visited[i]:
            visited[i] = True
            queue.append(i)
print(dp[n])
