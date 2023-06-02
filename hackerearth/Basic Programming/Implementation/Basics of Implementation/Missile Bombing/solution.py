n = int(input())
m = int(input())
field = [[0] * (n + 2) for _ in range(n + 2)]
for _ in range(m):
    p, a, b, c, d = map(int, input().strip().split())
    for i in [a - 1, c]:
        for j in [b - 1, d]:
            field[i][j] ^= p
for i in range(n, -1, -1):
    for j in range(n, -1, -1):
        field[i][j] ^= field[i + 1][j] ^ field[i][j + 1] ^ field[i + 1][j + 1]
for i in range(1, n + 1):
    print(' '.join(map(str, field[i][1: n + 1])))
