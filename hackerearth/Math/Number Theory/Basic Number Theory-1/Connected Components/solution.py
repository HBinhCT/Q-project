from sys import stdin

mod = 1000000007


def combine(comb, inv_comb, x, y):
    return comb[x] * (inv_comb[x - y] * inv_comb[y] % mod) % mod


t = int(stdin.readline())
cases = []
size = 0
for _ in range(t):
    n, m, c = map(int, stdin.readline().strip().split())
    cases.append((n, m, c))
    size = max(size, n, m, c)
fac = [1, 1]
size += 2
for i in range(2, size):
    fac.append(fac[i - 1] * i % mod)
inverse_fac = [0] * (size + 1)
inverse_fac[size] = pow(fac[size - 1] * size % mod, mod - 2, mod)
for i in range(size, 0, -1):
    inverse_fac[i - 1] = inverse_fac[i] * i % mod
for n, m, c in cases:
    if n == m and not c:
        print(1)
    elif not c or c + c - 1 > n or c > m + 1 or c > n - m:
        print(0)
    else:
        print(combine(fac, inverse_fac, m + 1, c) * combine(fac, inverse_fac, n - m - 1, c - 1) % mod)
