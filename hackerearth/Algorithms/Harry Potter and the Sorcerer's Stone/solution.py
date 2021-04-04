"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque

x1, y1, x2, y2 = map(int, input().strip().split())
dx = [2, -2, 2, -2, 1, 1, -1, -1]
dy = [1, 1, -1, -1, 2, -2, 2, -2]
visited = [[False] * 8 for _ in range(8)]
poss = [[0] * 8 for _ in range(8)]
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
q = deque()
q.append((x1, y1))
visited[x1][y1] = True
while q:
    x, y = q.popleft()
    for i in range(8):
        px = x + dx[i]
        py = y + dy[i]
        if 0 <= px < 8 and 0 <= py < 8 and not visited[px][py]:
            visited[px][py] = True
            poss[px][py] = poss[x][y] + 1
            q.append((px, py))
print(poss[x2][y2])
