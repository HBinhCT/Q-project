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
dp = [[0] * (n + 1) for _ in range(11)]
for i, v in enumerate(a, start=1):
    update(dp, n, len(set(str(v))), i, 1)
q = int(input())
for _ in range(q):
    t, *data = map(int, input().strip().split())
    if t in (0, 1):
        u, v = data
        w = u - 1
        update(dp, n, len(set(str(a[w]))), u, -1)
        a[w] += v - a[w] * t
        update(dp, n, len(set(str(a[w]))), u, 1)
    elif 2 == t:
        l, r, c = data
        print(query(dp, c, r) - query(dp, c, l - 1))
