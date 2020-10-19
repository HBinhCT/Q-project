def solve(n, h, i, u):
    arr = [[0] * (h + 1) for _ in range(n)]
    for x in range(n):
        for y in u[x][1:]:
            arr[x][y] += 1

    dp = [[0] * (h + 1) for _ in range(n)]
    opt = [0] * (h + 1)
    for x in range(1, h + 1):
        for y in range(n):
            dp[y][x] = dp[y][x - 1] + arr[y][x]
            if x >= i:
                dp[y][x] = max(dp[y][x], opt[x - i] + arr[y][x])
            opt[x] = max(opt[x], dp[y][x])
    return opt[h]


if __name__ == '__main__':
    n, h, i = map(int, input().strip().split())
    u = []
    for _ in range(n):
        u.append(list(map(int, input().strip().split())))
    print(solve(n, h, i, u))
