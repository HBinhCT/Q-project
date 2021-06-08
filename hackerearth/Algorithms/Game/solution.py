"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque


def trigger(x, y, ln, adjacency, seen, counter):
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    queue = deque([(x, y)])
    fireworks = set()
    empty_cells = {(x, y)}
    while queue:
        u, v = queue.pop()
        for du, dv in moves:
            nu, nv = u + du, v + dv
            if 0 <= nu < ln and 0 <= nv < ln:
                if adjacency[nu][nv] == '.' and not seen[nu][nv]:
                    seen[nu][nv] = True
                    queue.appendleft((nu, nv))
                    empty_cells.add((nu, nv))
                elif adjacency[nu][nv] == '*':
                    fireworks.add((nu, nv))
    count = len(fireworks)
    for x, y in empty_cells:
        counter[x][y] = count


n = int(input())
grid = []
for _ in range(n):
    grid.append(input().strip())
visited = [[False] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            dp[i][j] = 1
        elif not visited[i][j]:
            trigger(i, j, n, grid, visited, dp)
ans = 0
for i in range(n):
    for j in range(n):
        ans += dp[i][j]
print(ans)
