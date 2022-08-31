from sys import stdin
from threading import Thread

mod = 1000000007


def update(array, index, value):
    array[index] = value
    while index > 1:
        array[index >> 1] = (array[index] + array[index ^ 1]) % mod  # x ^ 1 = x - 1 if x % 2 else x + 1
        index >>= 1


def compute(array, start, end):
    res = 0
    while start < end:
        if start & 1:  # x & 1 = x % 2
            res = (array[start] + res) % mod
            start += 1
        if end & 1:
            end -= 1
            res = (array[end] + res) % mod
        start >>= 1  # x >> 1 = x / 2
        end >>= 1
    return res


def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    q = int(stdin.readline())
    queries = []
    m = max(a)
    for _ in range(q):
        t, x, y = stdin.readline().strip().split()
        x = int(x)
        y = int(y)
        m = max(m, y)
        queries.append((t, x, y))
    m += 1
    fx = list(range(m))
    for i in range(2, m):
        if fx[i] == i:
            fx[i] = i - 1
            for j in range(2 * i, m, i):
                fx[j] -= fx[j] // i
    sum_fx = [0] * m
    for i in range(1, m):
        k = 1
        for j in range(i, m, i):
            sum_fx[j] += i * fx[k]
            k += 1
    sum_fx_a = [sum_fx[i] for i in a]
    tree = [0] * (n * 3)
    for i in range(n):
        tree[n + i] = sum_fx_a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = (tree[i << 1] + tree[i << 1 | 1]) % mod  # x << 1 = x * 2; x | 1 = x if x % 2 else x + 1
    for t, x, y in queries:
        if t == 'C':
            print(compute(tree, x - 1 + n, y + n))
        elif t == 'U':
            update(tree, x - 1 + n, sum_fx[y])


thread = Thread(target=solve)
thread.start()
thread.join()
