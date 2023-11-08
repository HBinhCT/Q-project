from bisect import bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    m = n // 2
    total = sum(a)
    bc = set()
    for i in range(1 << m):
        score = 0
        for j in range(m):
            if 1 << j & i:
                score += a[j]
        bc.add(score)
    bc = sorted(bc)
    diff = float("inf")
    o = n - m
    p = len(bc)
    q = total // 2
    for i in range(1 << o):
        score = 0
        for j in range(o):
            if 1 << j & i:
                score += a[m + j]
        k = bisect_left(bc, q - score)
        for j in filter(lambda x: 0 <= x < p, (k - 1, k, k + 1)):
            diff = min(diff, abs(total * (total - 2 * (score + bc[j]))))
    print(diff)
