t = int(input())
for _ in range(t):
    x, y, n, w, p1, p2 = list(map(int, input().strip().split()))
    p1 /= 100
    p2 /= 100
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            pr1, pr2 = 0, 0
            if x >= j:
                pr1 = p1 + dp[i - 1][j] * (1.0 - p1)
            else:
                pr1 = dp[i - 1][j - x] * p1 + dp[i - 1][j] * (1.0 - p1)
            if y >= j:
                pr2 = p2 + dp[i - 1][j] * (1.0 - p2)
            else:
                pr2 = dp[i - 1][j - y] * p2 + dp[i - 1][j] * (1.0 - p2)
            dp[i][j] = max(pr1, pr2)
    print(f'{dp[n][w] * 100:.6f}')
