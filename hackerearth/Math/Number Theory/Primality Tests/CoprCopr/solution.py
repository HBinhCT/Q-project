from functools import lru_cache


@lru_cache(maxsize=None)
def f(x):
    a = x * x
    i = x
    while i > 1:
        j = x // i
        k = x // (j + 1)
        a -= f(j) * (i - k)
        i = k
    return a


t = int(input())
for _ in range(t):
    n = int(input())
    print((f(n) + 1) // 2)
