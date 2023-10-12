t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    ans = i = 0
    while i < n:
        if i < n - 1:
            if a[i] % 2 and a[i + 1] % 2:
                ans += 1
                i += 2
            elif a[i] % 2:
                ans += 2
                i += 2
            else:
                i += 1
        else:
            if a[i] % 2:
                ans += 2
            i += 2
    print(ans)
