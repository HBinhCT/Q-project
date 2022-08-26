def update(array, index, value=0):
    array[index] = value
    while index > 1:
        index //= 2
        array[index] = array[2 * index] + array[2 * index + 1]


def get_index(array, length, value):
    idx = 1
    if array[idx] < value:
        return -1
    while idx < length:
        tmp = array[2 * idx]
        if tmp >= value:
            idx *= 2
        else:
            idx = idx * 2 + 1
            value -= tmp
    return idx - length + 1


n = int(input())
q = int(input())
ln = 1 << n.bit_length()
a = [1 if i < n else 0 for i in range(ln)]
data = [0] * 2 * ln
data[ln:] = a
for i in range(ln - 1, -1, -1):
    data[i] = data[2 * i] + data[2 * i + 1]
for _ in range(q):
    operation, ik = map(int, input().strip().split())
    if operation == 0:
        update(data, ik - 1 + ln)
    elif operation == 1:
        print(get_index(data, ln, ik))
