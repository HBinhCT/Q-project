from sys import stdin
from collections import defaultdict

n, q = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
differences = defaultdict(list)
j = 0
prev_diff = diff = a[1] - a[0]
for i in range(1, n):
    diff = a[i] - a[i - 1]
    if diff != prev_diff:
        differences[prev_diff].append((j, i, i - j))
        j = i - 1
        prev_diff = diff
differences[diff].append((j, n, n - j))
for _ in range(q):
    l, r, d = map(int, stdin.readline().strip().split())
    l -= 1
    if l == r or d not in differences:
        print(1)
    else:
        ans = 1
        for start, end, length in differences[d]:
            if end <= l:
                continue
            elif l <= start and r >= end:
                ans = max(ans, length)
            elif start <= l <= end:
                ans = max(ans, min(r, end) - l)
            elif start <= r <= end:
                ans = max(ans, r - start)
            else:
                break
        print(ans)
