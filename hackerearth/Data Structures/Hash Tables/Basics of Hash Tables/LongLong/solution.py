from functools import reduce

mod = 2 ** 63 - 1


def check(k, a, n):
    p = pow(26, k, mod)
    x = reduce(lambda u, v: (u * 26 + v) % mod, a[:k], 0)
    visited = {x}
    for i in range(k, n):
        x = (x * 26 + a[i] - a[i - k] * p) % mod
        if x in visited:
            return i - k + 1
        visited.add(x)


s = input().strip()
idxes = [ord(c) - 97 for c in s]  # 97 is ord('a')
low = 0
high = ln = len(s)
while low < high:
    mid = (low + high + 1) // 2
    if check(mid, idxes, ln):
        low = mid
    else:
        high = mid - 1
print(low)
