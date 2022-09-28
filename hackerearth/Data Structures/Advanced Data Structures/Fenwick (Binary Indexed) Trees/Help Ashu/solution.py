def update(array, length, index, value):
    while index <= length:
        array[index] += value
        index += index & -index


def query(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


n = int(input())
a = list(map(int, input().strip().split()))
bit = [0] * (n + 1)
for i, v in enumerate(a, start=1):
    if v % 2 == 0:
        update(bit, n, i, 1)
q = int(input())
for _ in range(q):
    t, x, y = map(int, input().strip().split())
    if 0 == t:
        if a[x - 1] % 2 == 0:
            if y % 2 == 1:
                update(bit, n, x, -1)
        else:
            if y % 2 == 0:
                update(bit, n, x, 1)
        a[x - 1] = y
    elif 1 == t:
        print(query(bit, y) - query(bit, x - 1))
    elif 2 == t:
        print(y - x + 1 - (query(bit, y) - query(bit, x - 1)))
