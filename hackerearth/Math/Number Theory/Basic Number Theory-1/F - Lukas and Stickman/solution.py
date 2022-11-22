from collections import Counter
from sys import stdin

mod = 1000000007
n = int(stdin.readline())
a = list(map(int, stdin.readline().strip().split()))
s = set(a)
count = Counter(a)
res = 0
for a in s:
    for b in s:
        if a != b:
            mul = count[a] * count[b] % mod
        else:
            mul = count[a] * (count[b] - 1) % mod
        mul = mul * (a + b - 2) % mod
        tmp1 = (a - 1) * (a - 2) // 2 % mod
        tmp2 = (b - 1) * (b - 2) // 2 * (b - 3) // 3 % mod
        res += mul * tmp1 * tmp2 % mod
res = res * pow(n - 2, mod - 2, mod) % mod
print(res)
