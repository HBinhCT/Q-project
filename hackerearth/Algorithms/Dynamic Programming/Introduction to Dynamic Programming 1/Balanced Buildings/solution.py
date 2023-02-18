def get_cost(x, y, incr, decr):
    if x > y:
        return (x - y) * decr
    return (y - x) * incr


n, s, m, p = map(int, input().strip().split())
heights = list(map(int, input().strip().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
for j in range(n):
    dp[0][j] = -get_cost(heights[0], heights[j], p, m)
for i in range(1, n):
    max_cost = 0
    for j in range(n):
        max_cost = max(max_cost, dp[i - 1][j])
    for j in range(n):
        dp[i][j] = max(max_cost, dp[i - 1][j] + s) - get_cost(heights[i], heights[j], p, m)
print(max(dp[n - 1]))
