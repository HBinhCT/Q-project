from math import ceil, log
from sys import stdin


def segment(array, length):
    def generate(start, end, idx=0):
        if start == end:
            dp[idx] = array[start]
            return dp[idx]
        mid = (start + end) // 2
        dp[idx] = max(generate(start, mid, idx * 2 + 1), generate(mid + 1, end, idx * 2 + 2))
        return dp[idx]

    x = ceil(log(length, 2))
    m = 2 * pow(2, x) - 1
    dp = [0] * m
    generate(0, length - 1)
    return dp


def query(dp, length, left, right):
    def get_max(start, end, idx=0):
        if left <= start and right >= end:
            return dp[idx]
        if end < left or start > right:
            return 0
        mid = (start + end) // 2
        return max(get_max(start, mid, idx * 2 + 1), get_max(mid + 1, end, idx * 2 + 2))

    if left > right:
        return 0
    return get_max(0, length - 1)


t = int(stdin.readline())
for _ in range(t):
    n, q = map(int, stdin.readline().strip().split())
    a = list(map(int, stdin.readline().split()))
    counter = dict()
    prev = a[0]
    count = count_diff = 0
    for i, v in enumerate(a):
        if v != prev:
            counter[prev] = (count, i - count, count_diff)
            count = 1
            count_diff += 1
        else:
            count += 1
        prev = v
    if count:
        counter[prev] = (count, n - count, count_diff)
    vals = list(map(lambda x: x[1][0], sorted(counter.items())))
    size = len(counter)
    ans = segment(vals, size)
    for _ in range(q):
        l, r = [int(i) - 1 for i in stdin.readline().strip().split()]
        size_range = r - l + 1
        count, no, diff = counter[a[l]]
        begin = diff + 1
        min_left = min(no + count - l, size_range)
        _, no, diff = counter[a[r]]
        finish = diff - 1
        min_right = min(r - no + 1, size_range)
        print(max(min_left, query(ans, size, begin, finish), min_right))
