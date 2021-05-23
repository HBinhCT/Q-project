"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque


def find_path(x, y, rows, cols, grid):
    q = deque([(x, y, 0)])
    grid[x][y] = 1
    directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
    while q:
        x, y, ln = q.popleft()
        if x in (0, rows - 1) or y in (0, cols - 1):
            return ln
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not grid[nx][ny]:
                q.append((nx, ny, ln + 1))
                grid[nx][ny] = 1
    return -1


n, m = map(int, input().strip().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().strip().split())))
for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            print(find_path(i, j, n, m, g))
            break
    else:
        continue
    break
