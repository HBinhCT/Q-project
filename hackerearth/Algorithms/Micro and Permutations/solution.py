"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
n, m = map(int, input().strip().split())
edges = [[False] * n for _ in range(n)]
for _ in range(m):
    x, y = map(lambda z: int(z) - 1, input().strip().split())
    edges[x][y] = True
    edges[y][x] = True
ln = 1 << n
dp = [[False] * ln for _ in range(n)]
max_weights = [[0] * ln for _ in range(n)]
for i in range(n):
    dp[i][1 << i] = True
    max_weights[i][1 << i] = 1
for i in range(1 << n):
    for j in range(n):
        if i & 1 << j:
            for k in range(n):
                if i & 1 << k and j != k and edges[k][j] and dp[k][i ^ 1 << j]:
                    dp[j][i] = True
                    max_weights[j][i] += max_weights[k][i ^ 1 << j]
res = 0
for i in range(n):
    if dp[i][(1 << n) - 1]:
        res += max_weights[i][(1 << n) - 1]
print(res)
