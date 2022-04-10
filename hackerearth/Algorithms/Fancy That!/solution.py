from math import log10, floor

t = int(input())
for _ in range(t):
    l, r = map(int, input().strip().split())
    ans = 0
    x = l
    while x <= r:
        d = 10 ** floor(log10(x))
        m = floor(x / d)
        while m <= 8:
            y = (m + 1) * d
            if m % 2 == 0:
                ans += min(y, r + 1) - x
            m += 1
            x = y
            if x > r:
                break
        x = 10 ** (floor(log10(x)) + 1)
    print(ans)
