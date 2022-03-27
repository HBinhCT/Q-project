t = int(input())
for _ in range(t):
    n, m, k = map(int, input().strip().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().strip().split())))
    totals = [[[] for _ in range(m)] for _ in range(n)]
    totals[0][0] = [grid[0][0]]
    for i in range(1, m):
        totals[0][i] = [totals[0][i - 1][0] + grid[0][i]]
    for i in range(1, n):
        totals[i][0] = [totals[i - 1][0][0] + grid[i][0]]
    for i in range(1, n):
        for j in range(1, m):
            absorb = set()
            orb = grid[i][j]
            for power in totals[i][j - 1]:
                kii = orb + power
                if kii <= k:
                    absorb.add(kii)
            for power in totals[i - 1][j]:
                kii = orb + power
                if kii <= k:
                    absorb.add(kii)
            for power in totals[i - 1][j - 1]:
                kii = orb + power
                if kii <= k:
                    absorb.add(kii)
            totals[i][j] = sorted(absorb)
    ans = totals[n - 1][m - 1]
    if not ans or max(ans) > k:
        print(-1)
    else:
        print(max(ans))
