from sys import stdin

n, m = map(int, stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, stdin.readline().strip().split())))
coordinates = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
pluses = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        cells = tuple(a[i + x][j + y] for x, y in coordinates)
        pluses.append((sum(cells), i, j, cells))
pluses.sort(reverse=True)
ln = len(pluses)
max_sum = 0
for i in range(ln):
    if pluses[i][0] ** 2 <= max_sum:
        break
    max_cell = max(pluses[i][-1])
    for j in range(i + 1, ln):
        if max_cell * pluses[j][0] <= max_sum:
            break
        if abs(pluses[i][1] - pluses[j][1]) + abs(pluses[i][2] - pluses[j][2]) <= 1:
            continue
        total = sum(pluses[i][-1][k] * pluses[j][-1][k] for k in range(5))
        max_sum = max(max_sum, total)
print(max_sum)
