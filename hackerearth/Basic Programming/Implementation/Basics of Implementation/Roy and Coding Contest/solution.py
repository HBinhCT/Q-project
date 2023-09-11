from math import ceil

t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    if n == 1:
        print("0")
    else:
        count = res = 1
        while count < m and count < n:
            count *= 2
            res += 1
        if count > n:
            count /= 2
            res -= 1
        res += ceil((n - count) / m)
        print(res)
