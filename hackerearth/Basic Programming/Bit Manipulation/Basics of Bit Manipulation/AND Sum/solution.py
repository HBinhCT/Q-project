mod = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = 0
    x = 1
    for i in range(30):
        y = 0
        for j in arr:
            if j & x:
                y += 1
        ans = (ans + (2**y - 1) * x) % mod
        x <<= 1
    print(ans)
