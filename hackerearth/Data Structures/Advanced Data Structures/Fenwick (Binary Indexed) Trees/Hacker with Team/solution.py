def update(array, index, value):
    length = len(array)
    while index < length:
        array[index] += value
        index += index & (index ^ (index - 1))


def get_total(array, index):
    total = 0
    while index > 0:
        total += array[index]
        index -= index & (index ^ (index - 1))
    return total


def calc_left(array1, array2, left, right):
    res = get_total(array2, right) - get_total(array2, left)
    res += (get_total(array1, right) - get_total(array1, left)) * (1 - left)
    return res


def calc_right(array1, array2, left, right):
    res = get_total(array2, left) - get_total(array2, right)
    res += (get_total(array1, right) - get_total(array1, left)) * right
    return res


n, q = map(int, input().strip().split())
s = list(map(int, input().strip().split()))
tree1 = [0] * (n + 10)
tree2 = [0] * (n + 10)
for i, v in enumerate(s, start=1):
    update(tree1, i, v)
    update(tree2, i, (i - 1) * v)
for _ in range(q):
    o, *query = map(int, input().strip().split())
    query[0] -= 1
    if o == 1:
        l, r, k = query
        dist = min(k + 1, r - l)
        start = l - k + dist - 1
        end = max(l, r - k)
        ans = (get_total(tree1, end) - get_total(tree1, start)) * dist
        ans += calc_left(tree1, tree2, l - k, start) + calc_right(tree1, tree2, end, r)
        print(ans)
    elif o == 2:
        i, x = query
        j = i + 1
        diff = x - s[i]
        update(tree1, j, diff)
        update(tree2, j, i * diff)
        s[i] = x
