"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque

n, m, q = map(int, input().strip().split())
grid = []
for _ in range(n):
    grid.append(input().strip())
si, sj = map(lambda x: int(x) - 1, input().strip().split())
dist = [[-1] * m for _ in range(n)]
queue = deque([(si, sj)])
dist[si][sj] = 0
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
while queue:
    x, y = queue.popleft()
    for mx, my in moves:
        nx = x + mx
        ny = y + my
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '*' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
for _ in range(q):
    di, dj = map(lambda x: int(x) - 1, input().strip().split())
    print(dist[di][dj])
