mod = 1000000007


def prime_factors(x):
    factors = {}
    i = 2
    while i * i <= x:
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                x //= i
                cnt += 1
            factors[i] = cnt
        i += 1
    if x > 1:
        factors[x] = 1
    return factors


n = int(input())
f = prime_factors(n)
t = 1
for v in f.values():
    t *= v + 1
ans = 1
for a, b in f.items():
    v = pow(a - 1, b, mod) * pow(a, b * (b - 1) // 2, mod) % mod
    ans = ans * pow(v, t // (b + 1), mod) % mod
print(ans)
