mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    dp = [0] * 1001
    dp[0] = 1
    cnt = 0
    for i, (x, y) in enumerate(sorted(zip(a, b))):
        for j in range(min(len(dp), x - y + 1)):
            cnt += dp[j]
            cnt %= mod
        for j in range(len(dp) - 1, y - 1, -1):
            dp[j] += dp[j - y]
            dp[j] %= mod
    print(cnt)
