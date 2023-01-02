mod = 1000000007
n, m = map(int, input().strip().split())
fac = [1]
inverse_fac = [1]
for i in range(2, n + 1):
    fac.append((fac[-1] * i) % mod)
    inverse_fac.append(pow(fac[-1], mod - 2, mod))
for i in range(n + 1, 2 * n + 1):
    fac.append((fac[-1] * i) % mod)
h = 0
for _ in range(m):
    x, l = map(int, input().strip().split())
    for i in range(x + 1, x + l):
        t = fac[n - 1] * inverse_fac[i - 1] % mod * inverse_fac[n - i - 1] % mod
        h = (h + t * t % mod) % mod
t = fac[2 * n - 1] * inverse_fac[n - 1] * inverse_fac[n - 1] % mod
print((t - h) % mod)
