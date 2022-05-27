from sys import stdin

n, m, k = map(int, stdin.readline().strip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, stdin.readline().strip().split())))
applying = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c, s, d = map(int, stdin.readline().strip().split())
    r -= 1
    c -= 1
    j = c + s
    for i in range(r, min(r + s, n)):
        applying[i][c] += d
        if j < m:
            applying[i][j] -= d
for i in range(n):
    tot = 0
    for j in range(m):
        tot += applying[i][j]
        matrix[i][j] += tot
    print(*matrix[i])
