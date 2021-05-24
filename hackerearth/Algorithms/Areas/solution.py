"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque


def find(x, y, max_x, max_y, adjacency):
    queue = deque([(x, y)])
    total = 0
    cells = ((-1, 0), (0, -1), (0, 1), (1, 0))
    while queue:
        u, v = queue.popleft()
        total += 1
        for du, dv in cells:
            nu = u + du
            nv = v + dv
            if 0 <= nu < max_x and 0 <= nv < max_y and adjacency[nu][nv] == '.':
                adjacency[nu][nv] = '#'
                queue.append((nu, nv))
    return total


t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                res = find(i, j, n, m, grid)
                ans.append(res)
    ans.sort()
    print(len(ans))
    print(*ans)
