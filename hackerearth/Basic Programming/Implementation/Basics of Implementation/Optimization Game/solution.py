t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    ans = f = 0
    for i in a:
        q, r = divmod(i + f, 2)
        ans += r
        f = q
    while f:
        q, r = divmod(f, 2)
        ans += r
        f = q
    print(ans)
