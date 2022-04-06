t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().strip().split())))
    longest_path = 1
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not i and not j:
                dp[i][j] = 1
            elif not i and j:
                if a[i][j] > a[i][j - 1] and dp[i][j - 1]:
                    dp[i][j] = 1 + dp[i][j - 1]
                    longest_path = max(longest_path, dp[i][j])
            elif i and not j:
                if a[i][j] > a[i - 1][j] and dp[i - 1][j]:
                    dp[i][j] = 1 + dp[i - 1][j]
                    longest_path = max(longest_path, dp[i][j])
            else:
                x = y = 0
                if a[i][j] > a[i - 1][j]:
                    x = dp[i - 1][j]
                if a[i][j] > a[i][j - 1]:
                    y = dp[i][j - 1]
                if x or y:
                    dp[i][j] = 1 + max(x, y)
                    longest_path = max(longest_path, dp[i][j])
    print(longest_path)
