t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    s = []
    for _ in range(n):
        s.append(input().strip())
    build = [0]
    for i in range(1, n + 1):
        j = i - 1
        build.append(2 * build[j] + len(s[j]))
    ans = ""
    for _ in range(m):
        x = int(input())
        for i in range(n, 0, -1):
            j = i - 1
            if x >= 2 * build[j]:
                ans += s[j][x - 2 * build[j]]
                break
            elif x >= build[j]:
                x = 2 * build[j] - x - 1
    print(ans)
