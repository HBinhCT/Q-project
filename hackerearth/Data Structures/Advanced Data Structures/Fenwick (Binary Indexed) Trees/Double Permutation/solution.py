mod = 1000000007


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


n = int(input())
numbers = list(map(int, input().strip().split()))
if n < 2:
    print(1)
else:
    bit = [0] * (n + 1)
    check = [0] * (n + 1)
    lt = gt = 0
    for i, v in enumerate(numbers):
        tot = query(bit, v - 1)
        lt += tot
        gt += i - tot - check[v]
        check[v] = 1
        update(bit, n, v, 1)
    print((lt + n * 2 + gt * 3) * pow(2, n - 2, mod) % mod)
