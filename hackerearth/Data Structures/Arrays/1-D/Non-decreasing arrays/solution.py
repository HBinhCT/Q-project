from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = [a[0]]
    for i in range(1, n):
        x = ceil(b[-1] / a[i])
        b.append(x * a[i])
    print(*b)
