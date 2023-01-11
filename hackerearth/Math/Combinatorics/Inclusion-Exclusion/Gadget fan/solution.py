t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    ans = 0
    if k - n > 0:
        ans += n * min(n, k - n)
    start = k - min(n, k - 1)
    end = k - max(1, k - n + 1)
    if start <= end:
        ans += end * (end + 1) // 2 - start * (start - 1) // 2
    ans += min(n, k // 2)
    print(ans // 2)
