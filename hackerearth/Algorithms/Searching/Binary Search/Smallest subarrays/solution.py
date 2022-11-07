from sys import stdin


def update(array, length, index, value=1):
    while index <= length:
        array[index] += value
        index += index & -index


def query(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().strip().split()))
b = [0] + list(map(int, stdin.readline().strip().split()))
size1 = n + 1
size2 = n + 2
idxes = []
for i in range(1, size1):
    idxes.append((a[i], i))
idxes.sort(reverse=True)
idxes.insert(0, (0, 0))
bit = [0] * size1
ans = [-1] * size1
for i in range(1, size1):
    j = idxes[i][1]
    k = size1 - j
    update(bit, n, k)
    if b[j] <= size1 - j:
        t = query(bit, k)
        if b[j] <= t:
            low = 1
            high = k
            mn = t - b[j]
            while low < high:
                mid = (high + low) // 2
                if query(bit, mid) <= mn:
                    low = mid + 1
                else:
                    high = mid
            ans[j] = size2 - low - j
print(' '.join(map(str, ans[1:])))
