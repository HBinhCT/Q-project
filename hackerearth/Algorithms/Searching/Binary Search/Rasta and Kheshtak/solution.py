from collections import defaultdict
from sys import stdin

n, m = map(int, stdin.readline().strip().split())
a = []
for _ in range(n):
    a.append(list(map(int, stdin.readline().strip().split())))
x, y = map(int, stdin.readline().strip().split())
b = []
for _ in range(x):
    b.append(list(map(int, stdin.readline().strip().split())))
if a == b:
    print(n)
else:
    cells = defaultdict(list)
    x1 = 1000
    x2 = 1000000
    x3 = 1000000000
    for i in range(n - 1):
        for j in range(m - 1):
            row1 = a[i]
            row2 = a[i + 1]
            k = row1[j] * x3 + row1[j + 1] * x2 + row2[j] * x1 + row2[j + 1]
            cells[k].append((i, j))
    dp = [[0] * m for _ in range(n)]
    for i in range(x - 1):
        for j in range(y - 1):
            row1 = b[i]
            row2 = b[i + 1]
            k = row1[j] * x3 + row1[j + 1] * x2 + row2[j] * x1 + row2[j + 1]
            if k in cells:
                for u, v in cells[k]:
                    dp[u][v] = 1
    ans = 0
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j]:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])
                ans = max(ans, dp[i][j])
    print(ans + 1)
