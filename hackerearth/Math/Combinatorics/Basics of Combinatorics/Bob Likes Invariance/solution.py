mod = 1000000007
fac = [1] * 100001
for i in range(1, 100001):
    fac[i] = fac[i - 1] * i % mod
t = int(input())
for _ in range(t):
    n, z = map(int, input().strip().split())
    i = 1
    count = 0
    while i <= z:
        j = z // i
        if j < n:
            break
        count += fac[j - 1] * pow(fac[n - 1] * fac[j - n], mod - 2, mod)
        i += 1
    print(count % mod)
