from sys import stdin

mod = 1000000007
mod2 = 1000000005
inv4 = pow(4, mod2, mod)
inv6 = pow(6, mod2, mod)
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    n1 = n - 1
    w = n * n1 % mod
    minimum = w * n1 % mod * inv4 % mod
    maximum = w * (2 * n - 1) % mod * inv6 % mod
    print(minimum, maximum)
