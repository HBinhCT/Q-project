def find_ways(a, b, c, d):
    if abs(b - a) >= 2 and (a >= 11 or b >= 11):
        return -1
    if c < a or d < b:
        return -1
    if abs(c - d) != 2:
        return -1
    if c < 11 and d < 11:
        return -1
    n = d - b + 2
    m = c - a + 2
    dp = [[0] * n for _ in range(m)]
    u = b
    for i in range(1, n):
        dp[0][i] = u
        u += 1
    v = a
    for i in range(1, m):
        dp[i][0] = v
        v += 1
    for i in range(1, n):
        dp[1][i] = int(abs(dp[0][i] - dp[1][0]) < 2 or (dp[0][i] < 11 and dp[1][0] < 11))
    for i in range(1, m):
        dp[i][1] = int(abs(dp[i][0] - dp[0][1]) < 2 or (dp[i][0] < 11 and dp[0][1] < 11))
    for i in range(2, m):
        for j in range(2, n):
            if abs(dp[0][j] - dp[i][0]) < 2 or (dp[0][j] < 11 and dp[i][0] < 11):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0
    if d - b == 0:
        return dp[c - a][1]
    if c - a == 0:
        return dp[1][d - b]
    else:
        return dp[c - a][d - b + 1] + dp[c - a + 1][d - b]


t = int(input())
for i in range(1, t + 1):
    x1, x2, y1, y2 = map(int, input().strip().split())
    x = find_ways(x1, x2, y1, y2)
    print(f'Case {i}: {x % 1000000009 if x != -1 else x}')
