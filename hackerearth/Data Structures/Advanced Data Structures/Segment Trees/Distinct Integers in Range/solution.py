from sys import stdin


def prepare_data(array, length):
    data = [0] * length + [1 << (i - 1) for i in array]
    for i in reversed(range(length)):
        j = 2 * i
        data[i] = data[j] | data[j + 1]
    return data


def count(data, left, right):
    result = 0
    while left < right:
        if left & 1:
            result |= data[left]
            left += 1
        if right & 1:
            right -= 1
            result |= data[right]
        left >>= 1
        right >>= 1
    return result


n = int(stdin.readline())
array_a = list(map(int, stdin.readline().strip().split()))
array_b = list(map(int, stdin.readline().strip().split()))
data_a = prepare_data(array_a, n)
data_b = prepare_data(array_b, n)
q = int(stdin.readline())
for _ in range(q):
    a, b, c, d = [int(i) + n for i in stdin.readline().strip().split()]
    print(bin(count(data_a, a - 1, b) | count(data_b, c - 1, d)).count('1'))
