def search(array, val, length):
    def get_total(pos):
        pos += length
        total = 0
        while pos > 0:
            total += array[pos]
            pos //= 2
        return total

    left = -1
    right = length
    while right - left > 1:
        mid = (left + right) // 2
        res = get_total(mid)
        if res <= val:
            left = mid
        else:
            right = mid
    left += 1
    return left


def modify(array, left, right, val=-1):
    while left <= right:
        if left % 2:
            array[left] += val
            left += 1
        if not right % 2:
            array[right] += val
            right -= 1
        if left == right:
            break
        left //= 2
        right //= 2


def update(array, length):
    for k in range(1, length):
        array[2 * k] += array[k]
        array[2 * k + 1] += array[k]
        array[k] = 0


n = int(input())
a = list(map(int, input().strip().split()))
elements = sorted(zip(a, range(n)))
segment = [0] * 2 * n
for i in range(n):
    segment[i + n] = elements[i][0]
m = int(input())
end = 2 * n - 1
for _ in range(m):
    x = int(input())
    i = search(segment, x, n)
    if i != n:
        modify(segment, i + n, end)
update(segment, n)
final = [0] * n
for i in range(n):
    final[elements[i][1]] = segment[i + n]
print(' '.join(map(str, final)))
