"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque

n = int(input())
matrix = []
visited = [[False] * n for _ in range(n)]
s = (0, 0)
e = (0, 0)
for i in range(n):
    row = input().strip().split()
    matrix.append(row)
    for j in range(n):
        if row[j] == 'S':
            s = (i, j)
        elif row[j] == 'E':
            e = (i, j)
        elif row[j] == 'T':
            visited[i][j] = True
queue = deque([(s[0], s[-1], 0)])
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
while queue:
    x, y, count = queue.popleft()
    visited[x][y] = True
    if (x, y) == e:
        print(count)
        break
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            queue.append((nx, ny, count + 1))
