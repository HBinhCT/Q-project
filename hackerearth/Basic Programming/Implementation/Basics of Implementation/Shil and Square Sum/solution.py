mod = 1000000007
n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
a.insert(0, 0)
sq1 = sq2 = sq3 = 0
x = k * k % mod
y = 2 * k - 1
for i in range(1, k + 1):
    sq1 = (sq1 + i * i % mod * a[i]) % mod
    sq2 = (sq2 + (2 * i - 1) * a[i]) % mod
    sq3 = (sq3 + a[i]) % mod
print(sq1, end=' ')
for i in range(k + 1, n + 1):
    sq1 = (sq1 - sq2 + x * a[i]) % mod
    print(sq1, end=' ')
    sq2 = (sq2 - 2 * sq3 + a[i - k] + y * a[i]) % mod
    sq3 = (sq3 - a[i - k] + a[i]) % mod
