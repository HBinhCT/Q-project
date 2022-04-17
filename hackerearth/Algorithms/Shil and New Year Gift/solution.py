from math import gcd

n = int(input())
numbers = list(map(int, input().strip().split()))
lim = pow(2, n)
dp = [[0] * n for _ in range(lim)]
for i in range(lim):
    for j in range(n):
        if i & 1 << j:
            for k in range(n):
                if j != k and i & 1 << k:
                    dp[i][j] = max(dp[i][j], dp[i & ~(1 << j)][k] + gcd(numbers[k], numbers[j]))
print(max(dp[-1]))
