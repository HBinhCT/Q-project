from math import ceil, log
from sys import stdin

mod = 1000000007


def build(array, dp, start, end, idx=0):
    if start == end:
        dp[idx] = array[start]
    else:
        mid = (start + end) // 2
        idx1 = idx * 2 + 1
        idx2 = idx * 2 + 2
        build(array, dp, start, mid, idx1)
        build(array, dp, mid + 1, end, idx2)
        dp[idx] = dp[idx1] + dp[idx2]


def query(dp, start, end, left, right, idx=0):
    if left <= start and right >= end:
        return dp[idx]
    if right < start or left > end:
        return 0
    mid = (start + end) // 2
    return query(dp, start, mid, left, right, 2 * idx + 1) + query(dp, mid + 1, end, left, right, 2 * idx + 2)


def update(array, dp, start, end, pos, val, idx=0):
    if start == end:
        array[pos] += val
        dp[idx] += val
    else:
        mid = (start + end) // 2
        idx1 = idx * 2 + 1
        idx2 = idx * 2 + 2
        if start <= pos <= mid:
            update(array, dp, start, mid, pos, val, idx1)
        else:
            update(array, dp, mid + 1, end, pos, val, idx2)
        dp[idx] = dp[idx1] + dp[idx2]


r = int(stdin.readline())
n = int(stdin.readline())
a = list(map(int, stdin.readline().strip().split()))
last = n - 1
m = 2 ** (ceil(log(len(a), 2)))
tree = [0] * (2 * m - 1)
build(a, tree, 0, last)
for _ in range(r):
    x, w, d, y = map(int, stdin.readline().strip().split())
    x -= 1
    s = ceil(w / d)
    s = ((2 * w - (s - 1) * d) * s) // 2
    total_rotation = s // n
    s %= n
    count = query(tree, 0, last, 0, last) * total_rotation % mod
    if x + s > last:
        count += (query(tree, 0, last, x, last) + query(tree, 0, last, 0, (x + s) % n)) % mod
    else:
        count += query(tree, 0, last, x, x + s) % mod
    update(a, tree, 0, last, x, y)
    print(count % mod)
