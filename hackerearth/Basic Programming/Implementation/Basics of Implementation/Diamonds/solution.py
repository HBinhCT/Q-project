t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    floors = [input().strip().split() for _ in range(n)]
    ans = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if '/' == floors[i][j] and '\\' == floors[i][j + 1] and \
                    '\\' == floors[i + 1][j] and '/' == floors[i + 1][j + 1]:
                ans += 1
    print(ans)
