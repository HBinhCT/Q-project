def get_mod(x):
    return 1 + x % 2


def get_sum(array, length, index):
    pos = length - index
    total = 0
    while pos:
        total += array[pos]
        total %= 3
        pos -= pos & -pos
    return total


def update(array, length, index, value):
    if not value:
        return
    pos = length - index
    val = get_mod(pos - 1)
    while pos <= length:
        array[pos] += val
        array[pos] %= 3
        pos += pos & -pos


n = int(input())
binary_string = list(map(int, input().strip()))
bit = [0] * (n + 1)
for i, v in enumerate(binary_string):
    update(bit, n, i, v)
q = int(input())
for _ in range(q):
    t, *query = map(int, input().strip().split())
    if 0 == t:
        l, r = map(int, query)
        if r == n - 1:
            ans = get_sum(bit, n, l)
        else:
            ans = (get_sum(bit, n, l) - get_sum(bit, n, r + 1)) % 3 * get_mod(n - r - 1)
        print(ans % 3)
    elif 1 == t:
        l = query[0]
        if not binary_string[l]:
            binary_string[l] = 1
            update(bit, n, l, 1)
