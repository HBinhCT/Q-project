n, m = map(int, input().strip().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().strip().split())))
row_sums = list(map(sum, a))
col_sums = list(map(sum, zip(*a)))
pos = None
max_sum = float('-inf')
for i in range(n):
    for j in range(m):
        total = row_sums[i] + col_sums[j] - 2 * a[i][j]
        if total > max_sum:
            max_sum = total
            pos = (i + 1, j + 1)
print(*pos)
