def update(array, index, value):
    length = len(array)
    while index < length:
        array[index] += value
        index += index & -index


def query(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


def range_query(array, left, right):
    return query(array, right) - query(array, left - 1)


n, q = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
tree1 = [0] * (n + 1)
tree2 = [0] * (n + 1)
for i, v in enumerate(a, start=1):
    update(tree1, i, v)
    update(tree2, i, v * i)
for _ in range(q):
    t, *event = map(int, input().strip().split())
    if 1 == t:
        k, l, r = event
        if k > r:
            print(range_query(tree1, l, r) * k - range_query(tree2, l, r))
        elif k < l:
            print(range_query(tree2, l, r) - range_query(tree1, l, r) * k)
        else:
            print(range_query(tree2, k, r) - range_query(tree1, k, r) * k +
                  range_query(tree1, l, k) * k - range_query(tree2, l, k))
    elif 2 == t:
        k, s = event
        update(tree1, k, s)
        update(tree2, k, s * k)
