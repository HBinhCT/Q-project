mod = 1000000007
mod_2 = mod - 2
n = int(input())
res = 0
a = b = 1
for i in range(n + 1):
    res += (mod + a) * b * pow(2, ((n - i) * (n - i - 1)) >> 1, mod)
    res %= mod
    a *= -1
    b *= n - i
    b %= mod
    b *= pow(i + 1, mod_2, mod)
    b %= mod
print(res)
