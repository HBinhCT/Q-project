"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import deque


def check(adj, visited, i, j, k, n, m, h):
    moves = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
    queue = deque([(k, i, j)])
    res = 1
    cubic = []
    while len(queue) > 0:
        k, i, j = queue.pop()
        if not visited[k][i][j]:
            cubic.append((k, i, j))
            if res != -1 and i in (0, n - 1) or j in (0, m - 1) or k in (0, h - 1):
                res = -1
            visited[k][i][j] = res
            for dk, di, dj in moves:
                ni = i + di
                nj = j + dj
                nk = k + dk
                if 0 <= ni < n and 0 <= nj < m and 0 <= nk < h and not adj[nk][ni][nj] and not visited[nk][ni][nj]:
                    queue.append((nk, ni, nj))
    for k, i, j in cubic:
        if visited[k][i][j] != res:
            visited[k][i][j] = res


def find(adjacency, n, m, h):
    visited = [[[0] * m for _ in range(n)] for _ in range(h)]
    # 0 not visited, -1 visited but air can pass, 1 air cannot pass
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if not adjacency[k][i][j] and not visited[k][i][j]:
                    check(adjacency, visited, i, j, k, n, m, h)
    ans = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                ans += visited[k][i][j] == 1
    return ans


t = int(input())
for _ in range(t):
    x, y, z = map(int, input().strip().split())
    box = [[[] for _ in range(x)] for _ in range(z)]
    for k in range(z):
        for i in range(x):
            box[k][i] = (list(map(int, input().strip().split())))
    print(find(box, x, y, z))
