x = int(input())
n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().strip().split())
    a.append(ai)
    b.append(bi)
dp = [0] * (x + 1)
for i in range(x + 1):
    for j in range(n):
        if a[j] <= i:
            dp[i] = max(dp[i], dp[i - a[j]] + b[j])
print(dp[x])
