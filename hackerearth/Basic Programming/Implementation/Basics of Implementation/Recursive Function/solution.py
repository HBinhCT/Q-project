from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)


@lru_cache(maxsize=None)
def f(a, b):
    if 0 == a:
        return (b + 1) % 1000
    elif 0 == b:
        return f(a - 1, 1)
    else:
        return f(a - 1, f(a, b - 1))


x, y = map(int, input().strip().split())
print(str(f(x, y)).zfill(3))
