def query(array, index):
    total = 0
    while index > 0:
        total += array[index]
        index -= index & -index
    return total


def update(array, length, index, value):
    while index <= length:
        array[index] += value
        index += index & -index


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().strip().split()))
    tree = [0] * (n + 1)
    tot = 0
    for i in range(n):
        tot += i - query(tree, p[i] - 1)
        update(tree, n, p[i], 1)
    ans = tot
    for i in range(n - 1):
        tot += n - query(tree, p[i]) - query(tree, p[i] - 1)
        ans ^= tot
    print(ans)
