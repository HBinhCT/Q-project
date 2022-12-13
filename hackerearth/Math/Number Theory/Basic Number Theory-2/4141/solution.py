from sys import stdin


def check(x, y, a, b):
    visited = [[[-1] * 41 for _ in range(10)] for _ in range(10)]
    last = []
    i = z = 0
    while visited[x][y][z] < 0 and i <= b:
        last.append(z)
        visited[x][y][z] = i
        i += 1
        z = (z * 10 + x) % 41
        x, y = y, (y * a + x) % 10
    if b + 1 <= len(last):
        y = last[b]
    else:
        i = visited[x][y][z]
        j = len(last) - i
        y = last[b if b <= i else i + (b - i) % j]
    return 0 == y % 41


t = int(stdin.readline())
for _ in range(t):
    a0, a1, c, n = map(int, stdin.readline().strip().split())
    print('YES' if check(a0, a1, c, n) else 'NO')
