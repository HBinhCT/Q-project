mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    print(n * (2 * n - 1) % mod)
