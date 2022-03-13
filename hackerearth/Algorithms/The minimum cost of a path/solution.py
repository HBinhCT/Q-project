"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
mx = 100001
cost = [0] * mx
for i in range(2, mx):
    if not cost[i]:
        j = i
        while j < mx:
            for k in range(j, mx, j):
                cost[k] += 1
            j *= i
t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    cells = []
    for i in range(n):
        cells.append(list(map(int, input().strip().split())))
        for j in range(m):
            cells[i][j] = cost[cells[i][j]]
    dp = [[0] * m for _ in range(n)]
    dp[-1][-1] = cells[-1][-1]
    for i in range(n - 2, -1, -1):
        dp[i][-1] = cells[i][-1] + dp[i + 1][-1]
    for i in range(m - 2, -1, -1):
        dp[-1][i] = cells[-1][i] + dp[-1][i + 1]
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            dp[i][j] = cells[i][j] + min(dp[i + 1][j], dp[i][j + 1])
    print(dp[0][0])
