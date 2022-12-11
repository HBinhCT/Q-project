n = int(input())
mod = 1000000007
x = int(n ** .5)
b = x * (x + 1) * (2 * x + 1) // 6
a = 0
for i in range(1, x + 1):
    j = n // i
    a += i * (i + j) * (j - i + 1)
print((a - b) % mod)
