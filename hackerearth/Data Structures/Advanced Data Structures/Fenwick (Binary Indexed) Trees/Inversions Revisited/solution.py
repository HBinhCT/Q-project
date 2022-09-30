def query(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


def update(array, index, value):
    length = len(array)
    while index < length:
        array[index] += value
        index += index & -index


n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
bit = [0] * (max(a) + 1)
ans = 0
for i in range(n - 1, -1, -1):
    ans += query(bit, a[i])
    update(bit, b[i] + 1, 1)
print(ans)
