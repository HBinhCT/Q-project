mod = 1000000007


def fact(num):
    res = 1
    for i in range(2, num + 1):
        res = res * i % mod
    return res


l, r, n = map(int, input().strip().split())
a = [max(int(i), 1) for i in input().strip().split()]
m = r - l + 1 - sum(a) + n - 1
if m < n:
    print(0)
else:
    x = fact(m)
    y = fact(n)
    z = fact(m - n)
    print((x * pow(y, mod - 2, mod) * pow(z, mod - 2, mod)) % mod)
