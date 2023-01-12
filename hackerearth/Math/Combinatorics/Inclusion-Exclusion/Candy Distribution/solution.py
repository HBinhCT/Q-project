mod = 1000000007
mod_2 = mod - 2
fac = [1]
for i in range(1, 1000001):
    fac.append(fac[-1] * i % mod)
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().strip().split())
    ans = fac[n] * pow(fac[x] * fac[n - x], mod_2, mod) % mod
    ans = ans * (x - y) % mod * pow(x + y, mod_2, mod) % mod
    print(ans)
