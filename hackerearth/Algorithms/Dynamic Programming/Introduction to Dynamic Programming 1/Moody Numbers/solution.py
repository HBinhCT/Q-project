from functools import lru_cache


@lru_cache(maxsize=None)
def sum_of_digits(x):
    x = x ** 2
    y = 0
    while x:
        y, x = y + x % 10, x // 10
    return y


@lru_cache(maxsize=None)
def f(x):
    if x == 1 or x == 4:
        return True
    if x == 9 or x == 13:
        return False
    return f(sum_of_digits(x))


t = int(input())
for _ in range(t):
    n = int(input())
    print('YES' if f(n) else 'NO')
