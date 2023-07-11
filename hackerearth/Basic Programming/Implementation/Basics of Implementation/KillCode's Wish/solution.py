t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    x = (max(a) - 1) // m * m
    idx = 0
    for i in range(n):
        if a[i] > x:
            idx = i
    print(idx + 1)
