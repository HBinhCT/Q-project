from collections import Counter

n = int(input())
a = list(map(int, input().strip().split()))
mod = 1000000007
counter = Counter(a)
ans = 0
for k, v in counter.items():
    if k:
        ans += 2 ** (v - 1) % mod
    else:
        ans += (2 ** v - 1) % mod
    ans %= mod
print(ans)
