def update(array, length, row, col, value):
    while row <= length:
        array[row][col] += value
        row += row & -row


def query(array, row, col):
    total = 0
    while row:
        total += array[row][col]
        row -= row & -row
    return total


n, q = map(int, input().strip().split())
s = list(input().strip())
bit = [[0] * 26 for _ in range(n + 1)]
for i, v in enumerate(s, start=1):
    update(bit, n, i, ord(v) - 97, 1)  # ord('a') = 97
for _ in range(q):
    t, *data = input().strip().split()
    t = int(t)
    if 1 == t:
        l, x = data
        l = int(l)
        update(bit, n, l, ord(x) - 97, 1)
        c = s[l - 1]
        update(bit, n, l, ord(c) - 97, -1)
        s[l - 1] = x
    else:
        l, r = map(int, data)
        count = 0
        for i in range(26):
            range_sum = query(bit, r, i) - query(bit, l - 1, i)
            count += range_sum % 2 != 0
            if count > 1:
                print('no')
                break
        else:
            print('yes')
