mod = 1000000007
rows = 101
cols = 10001
dp = [[1] * cols for _ in range(rows)]
for i in range(1, cols):
    dp[0][i] = 0
for i in range(2, rows):
    for j in range(2, cols):
        if i > j:
            dp[i][j] = dp[i - 1][j] % mod
        elif i == j:
            dp[i][j] = dp[i][j - 1] * 2 % mod
        else:
            dp[i][j] = (dp[i][j - 1] * 2 - dp[i][j - i - 1]) % mod


def solve(K, N):
    # write code here
    return dp[K][N]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    out_ = solve(K, N)
    print(out_)
