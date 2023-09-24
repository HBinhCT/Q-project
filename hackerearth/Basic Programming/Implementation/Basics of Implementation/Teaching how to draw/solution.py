n = int(input())
for _ in range(n):
    s = int(input())
    ans = 0
    for i in range(1, int(s**0.5) + 1):
        ans += s // i - (i - 1)
    print(ans)
