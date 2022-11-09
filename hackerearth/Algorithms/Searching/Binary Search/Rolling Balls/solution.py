from sys import stdin
from bisect import bisect_left, bisect

l, n, q = map(int, stdin.readline().strip().split())
s = [int(i) - 1 for i in stdin.readline().strip().split()]
d = list(map(int, stdin.readline().strip().split()))
l -= 1
right = []
for i in range(n):
    if d[i]:
        right.append(s[i])
        right.append(-2 * l + s[i])
        right.append(2 * l + s[i])
    else:
        right.append(-s[i])
        right.append(-2 * l - s[i])
        right.append(2 * l - s[i])
right.sort()
left = [-i for i in right[::-1]]
unique_left = set(left)
for _ in range(q):
    t, p = map(int, stdin.readline().strip().split())
    t %= 2 * l
    x = int(t in unique_left)
    y = bisect_left(left, 1 + t) + bisect_left(right, 1 - t)
    low = -1
    high = l
    while low < high:
        mid = (low + high) // 2
        if bisect(left, mid + t) + bisect(right, mid - t) - y + x >= p:
            high = mid
        else:
            low = mid + 1
    print(high + 1)
