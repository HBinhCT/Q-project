from functools import lru_cache


def update(array, idx, val):
    ln = len(array)
    while idx < ln:
        array[idx] += val
        idx += idx & -idx


@lru_cache(maxsize=None)
def is_prime(u):
    if u <= 1 or (u > 3 and (u % 2 == 0 or u % 3 == 0)):
        return False
    for v in range(5, int(u ** .5) + 1, 6):
        if u % v == 0 or u % (v + 2) == 0:
            return False
    return True


def get_total(array, idx):
    total = 0
    while idx > 0:
        total += array[idx]
        idx -= idx & -idx
    return total


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    segment = [0] * (n + 1)
    for i in range(n):
        update(segment, i + 1, is_prime(a[i]))
    q = int(input())
    for _ in range(q):
        p, x, y = input().strip().split()
        x = int(x)
        y = int(y)
        if p == 'C':
            if is_prime(a[x - 1]) and not is_prime(y):
                update(segment, x, -1)
            elif not is_prime(a[x - 1]) and is_prime(y):
                update(segment, x, 1)
            a[x - 1] = y
        elif p == 'A':
            print(get_total(segment, y) - get_total(segment, x - 1))
