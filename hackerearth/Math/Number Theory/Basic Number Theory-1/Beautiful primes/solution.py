from sys import stdin

mod = 1000000007
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    p = list(map(int, stdin.readline().strip().split()))
    the_sum = 1
    for i in range(n):
        the_sum = the_sum * a[i] % mod * (pow(a[i], p[i], mod) - 1) % mod * pow(a[i] - 1, mod - 2, mod) % mod
    print(the_sum)
