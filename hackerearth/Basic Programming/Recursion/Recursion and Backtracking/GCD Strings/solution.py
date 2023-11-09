mod = 1000000007


def f(a, b):
    if a % b:
        p, q = f(b, a % b)
        r = pow(2, b, mod)
        o = p * (pow(r, a // b) - 1) // (r - 1)
        o = o * pow(2, a % b, mod) % mod
        o = (o + q) % mod
        return o, p
    else:
        return pow(2, a - 1, mod), pow(2, b - 1, mod)


t = int(input())
for _ in range(t):
    x, y = map(int, input().strip().split())
    s, _ = f(x, y)
    print(s)
