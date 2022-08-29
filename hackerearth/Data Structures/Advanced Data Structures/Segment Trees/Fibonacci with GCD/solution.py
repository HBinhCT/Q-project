from functools import lru_cache
from math import ceil, log, gcd

mod = 1000000007


def segment(array, dp, start=0, end=None, idx=0):
    if end is None:
        end = len(array) - 1
    if start == end:
        dp[idx] = array[start]
        return array[start]
    mid = (start + end) // 2
    dp[idx] = gcd(segment(array, dp, start, mid, idx * 2 + 1), segment(array, dp, mid + 1, end, idx * 2 + 2))
    return dp[idx]


def query(dp, start, end, left, right, idx=0):
    if left <= start and right >= end:
        return dp[idx]
    if end < left or start > right:
        return -1
    mid = (start + end) // 2
    u = query(dp, start, mid, left, right, 2 * idx + 1)
    v = query(dp, mid + 1, end, left, right, 2 * idx + 2)
    if u == -1:
        return v
    if v == -1:
        return u
    return gcd(u, v)


@lru_cache(maxsize=None)
def fibonacci(x):
    if x <= 0:
        return 0
    if x <= 2:
        return 1
    if x % 2:
        k = (x + 1) // 2
        u = fibonacci(k - 1)
        v = fibonacci(k)
        return u * u % mod + v * v % mod
    else:
        k = x // 2
        u = fibonacci(k - 1)
        v = fibonacci(k)
        return (2 * u + v) * v % mod


n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
i = ceil(log(n, 2))
m = 2 * pow(2, i) - 1
ans = [0] * (m + 1)
segment(a, ans)
ln = n - 1
for _ in range(q):
    l, r = [int(i) - 1 for i in input().strip().split()]
    print((fibonacci(query(ans, 0, ln, l, r)) % mod))
