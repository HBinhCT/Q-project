t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    total = sum(a)
    if 0 == total or n == total:
        print(0)
        continue
    if n - total < n // 2:
        print(-1)
        continue
    ans = i = 0
    while i < n - 1:
        if a[i] == 1 and a[i + 1] == 1:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)
