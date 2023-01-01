n = int(input())
a = list(map(int, input().strip().split()))
m = 2 * n + 1
f = [0] * m
f[1] = 1
mod = 1000000007
for i in range(3, m):
    f[i] = f[i - 2] * i % mod
ans = 0
for i in range(2, m):
    cnt = f[n + n - 1]
    cnt = (cnt + mod - f[i - 2] * f[2 * n - i] % mod) % mod
    ans = (ans + cnt * (a[i - 1] - a[i - 2])) % mod
print(ans)
