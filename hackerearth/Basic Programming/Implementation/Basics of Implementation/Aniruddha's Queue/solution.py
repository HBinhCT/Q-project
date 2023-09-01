t = int(input())
for _ in range(t):
    n = int(input())
    distances = list(map(int, input().strip().split()))
    m = int(input())
    total = sum(distances)
    if m > total:
        m %= total
    ans = 0
    if m:
        for i in range(n):
            m -= distances[i]
            if 0 >= m:
                ans = i + 1
                break
    else:
        for i in range(n - 1, -1, -1):
            if distances[i]:
                ans = i + 1
                break
    print(ans)
