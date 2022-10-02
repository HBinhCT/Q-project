mod = 1000000007


def update(array, length, row, col, value):
    while col <= length:
        array[row][col] += value
        col += col & -col


def query(array, row, col):
    total = 0
    while col:
        total += array[row][col]
        col -= col & -col
    return total


n = int(input())
a = list(map(int, input().strip().split()))
lens = [0] * (n + 1)
dp = [[0] * (n + 1) for _ in range(11)]
for i, v in enumerate(a, start=1):
    lens[i] = len(set(str(v)))
    update(dp, n, lens[i], i, 1)
q = int(input())
for _ in range(q):
    t, *data = input().strip().split()
    if t in ('ADD', 'MUL', 'REP'):
        u, v = map(int, data)
        w = u - 1
        update(dp, n, lens[u], u, -1)
        if 'ADD' == t:
            a[w] = (a[w] + v) % mod
        elif 'MUL' == t:
            a[w] = (a[w] * v) % mod
        elif 'REP' == t:
            a[w] = v % mod
        lens[u] = len(set(str(a[w])))
        update(dp, n, lens[u], u, 1)
    elif t in ('MAX', 'MIN'):
        l, r = map(int, data)
        digits = range(0)
        if 'MAX' == t:
            digits = range(10, -1, -1)
        elif 'MIN' == t:
            digits = range(1, 11)
        for i in digits:
            val = query(dp, i, r)
            if val:
                val -= query(dp, i, l - 1)
            if val:
                print(i, val)
                break
        else:
            print(0, 0)
