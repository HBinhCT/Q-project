n, m = map(int, input().strip().split())
chart = []
for _ in range(n):
    chart.append(tuple(map(int, input().strip())))
dp = [[1] * m for _ in range(n)]
count = 0
for i in range(1, n):
    for j in range(1, m):
        if chart[i][j] != chart[i - 1][j] and chart[i][j] != chart[i][j - 1] and chart[i][j] == chart[i - 1][j - 1]:
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        if dp[i][j] >= 8:
            count += 1
print(count)
