def update(arr, all_length, idx, val):
    arr[idx] = val
    diff = len(val) - all_length[0][idx]
    for i in range(len(all_length)):
        all_length[i][idx] += diff
        idx //= 2


def get_len(all_length, idx):
    total = j = 0
    i = len(all_length) - 1
    while i >= 0:
        x = 1 << i  # x << y = x * pow(2, y)
        if idx >= x:
            idx -= x
            total += all_length[i][j]
            j += 1
            if j > len(all_length[i]):
                return total
        j *= 2
        i -= 1
    return total


def get_digit(arr, all_length, pos):
    j = 0
    i = len(all_length) - 1
    while i >= 0:
        if all_length[i][j] <= pos:
            pos -= all_length[i][j]
            j += 1
            if j > len(all_length[i]):
                return -1
        if i:
            j *= 2
        i -= 1
    return arr[j][pos]


n, m = map(int, input().strip().split())
a = input().strip().split()
lens = [len(i) for i in a]
all_len = [lens]
while len(lens) > 1:
    new_lens = [lens[2 * i] + lens[2 * i + 1] for i in range(len(lens) // 2)]
    if len(lens) % 2:
        new_lens.append(lens[-1])
    all_len.append(new_lens)
    lens = new_lens
for _ in range(m):
    p, *query = input().strip().split()
    if p == 'update':
        position, value = query
        update(a, all_len, int(position) - 1, value)
    if p == 'get':
        l, r, k = [int(i) - 1 for i in query]
        l1 = get_len(all_len, l)
        l2 = get_len(all_len, r + 1)
        if k >= l2 - l1:
            print(-1)
        else:
            print(get_digit(a, all_len, l1 + k))
