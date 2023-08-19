from bisect import bisect_left, bisect_right

t = int(input())
for _ in range(t):
    n, k, l, r = map(int, input().strip().split())
    dresses = input().strip()
    special = set(input().strip())
    a = [0] * (n + 1)
    for i, c in enumerate(dresses):
        a[i + 1] = a[i]
        if c in special:
            a[i + 1] += 1
    ways = 0
    for i in range(1, n + 1):
        if l <= a[i] and a[i] - a[i - 1] <= r:
            j1 = bisect_left(a, a[i] - r)
            j2 = min(bisect_right(a, a[i] - l), i) - 1
            ways += max(j2 - j1 + 1, 0)
    print(ways)
