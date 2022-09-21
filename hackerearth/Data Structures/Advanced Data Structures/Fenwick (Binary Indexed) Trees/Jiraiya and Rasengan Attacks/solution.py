mod = 1000000007


def update(array, index, value):
    length = len(array)
    while index < length:
        array[index] += value
        index += index & -index


def query(array, index):
    total = 0
    while index > 0:
        total += array[index]
        index -= index & -index
    return total


n = int(input())
p = list(map(int, input().strip().split()))
tree1 = [0] * (n + 10)
tree2 = [0] * (n + 10)
x = (n - 1) * n * (n + 1) * (n + 2) // 24
y = z = 0
for i, v in enumerate(p):
    z += (n - i) * (query(tree1, n) - query(tree1, v))
    y += query(tree2, n) - query(tree2, v)
    update(tree1, v, i + 1)
    update(tree2, v, 1)
x += y * n * (n + 1) // 2 - 2 * z
print(x * pow((n * (n + 1)) // 2, mod - 2, mod) % mod)
