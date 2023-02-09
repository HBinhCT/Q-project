from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    b = a.copy()
    dp = [[0] * 2 for i in range(n)]
    if a[0] % 2:
        while a[0] % 2:
            dp[0][0] += 1
            a[0] //= 2
    else:
        while not a[0] % 2:
            dp[0][1] += 1
            a[0] //= 2
    for i in range(1, n):
        j = i - 1
        x = y = 0
        if a[i] % 2:
            while a[i] % 2:
                x += 1
                a[i] //= 2
        else:
            while not a[i] % 2:
                y += 1
                a[i] //= 2
        if b[i] % 2:
            dp[i][0] = min(dp[j][0] + x, dp[j][1] + y + 1)
            dp[i][1] = dp[j][0] + y
        else:
            dp[i][0] = min(dp[j][0] + x, dp[j][1] + y + 1)
            dp[i][1] = min(dp[j][0] + y, dp[j][1] + x + 1)
    print(dp[n - 1][0])
