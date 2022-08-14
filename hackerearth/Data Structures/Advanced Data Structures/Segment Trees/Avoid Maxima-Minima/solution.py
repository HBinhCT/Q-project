def build(size):
    md = [[0]]
    while len(md[-1]) < size:
        md.append(md[-1] + md[-1])
    return md


def update(md, col, val):
    col -= 1
    row = len(md) - 1
    while row >= 0:
        if md[row][col] >= val:
            return
        md[row][col] = val
        row -= 1
        col >>= 1  # x >> 1 is equivalent to x / 2


def query(md, left, right):
    left -= 1
    right -= 1
    row = len(md) - 1
    res = 0
    while left <= right:
        if left & 1:  # x & 1 is equivalent to x % 2
            res = max(res, md[row][left])
            left += 1
        if not (right & 1):
            res = max(res, md[row][right])
            right -= 1
        left >>= 1  # x >> 1 is equivalent to x / 2
        right >>= 1
        row -= 1
    return res


def solve(arr, size):
    incs = build(size)
    decs = build(size)
    acts = build(size)
    for i in arr:
        imx = query(incs, 1, i)
        amx = query(acts, 1, i)
        iv = max(imx, decs[-1][i - 1], amx) + 1
        dmx = query(decs, i, size)
        amx = query(acts, i, size)
        dv = max(dmx, incs[-1][i - 1], amx) + 1
        update(acts, i, max(incs[-1][i - 1], decs[-1][i - 1]))
        update(incs, i, iv)
        update(decs, i, dv)
    return max(incs[0][0], decs[0][0])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(solve(a, n))
