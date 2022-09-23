from sys import stdin


def is_round(num):
    return num[0] == num[-1]


def query(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


def update(array, length, index, value):
    while index <= length:
        array[index] += value
        index += index & -index


n, q = map(int, stdin.readline().strip().split())
a = stdin.readline().strip().split()
tree = [0] * (n + 1)
for i, v in enumerate(a, start=1):
    if is_round(v):
        update(tree, n, i, 1)
for _ in range(q):
    t, *data = map(int, stdin.readline().strip().split())
    if 1 == t:
        l, r = data
        print(query(tree, r) - query(tree, l - 1))
    elif 2 == t:
        i, k = data
        is_prev_round = query(tree, i) - query(tree, i - 1) == 1
        is_curr_round = is_round(str(k))
        if is_prev_round and not is_curr_round:
            update(tree, n, i, -1)
        if not is_prev_round and is_curr_round:
            update(tree, n, i, 1)
