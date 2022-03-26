mod = 1000000009
dp = [[0] * 1001 for _ in range(1001)]
for i in range(1, 1001):
    for j in range(1000, -1, -1):
        if i < j:
            dp[i][j] = 0
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j + 1] + dp[i - j][j]
            dp[i][j] %= mod
t = int(input())
for _ in range(t):
    a, s = map(int, input().strip().split())
    print(dp[a][s])
