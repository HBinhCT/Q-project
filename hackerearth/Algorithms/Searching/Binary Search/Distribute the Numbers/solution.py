def check(n, d1, d2, p1, p2):
    a = n // p1
    b = n // p2
    c = n // (p1 * p2)
    d1 = max(0, d1 - (b - c))
    d2 = max(0, d2 - (a - c))
    n = max(0, n - (a + b - c))
    return n >= d1 + d2


t = int(input())
for _ in range(t):
    n1, n2, x, y = map(int, input().strip().split())
    left, right = 1, 1000000000000000000
    while left <= right:
        mid = (left + right) // 2
        if check(mid, n1, n2, x, y):
            right = mid - 1
        else:
            left = mid + 1
    print(left)
