from collections import Counter

n, r, c = map(int, input().strip().split())
matrix = []
for _ in range(n):
    matrix.append(input().strip().split())
rows = [int(i) - 1 for i in input().strip().split()]
cols = [int(i) - 1 for i in input().strip().split()]
c_rows = Counter(rows)
for i in c_rows:
    j = c_rows[i] % n
    if j:
        matrix[i] = matrix[i][n - j:] + matrix[i][:n - j]
c_cols = Counter(cols)
for j in c_cols:
    k = c_cols[j] % n
    if k:
        rotate = [matrix[i][j] for i in range(n - k, n)] + [matrix[i][j] for i in range(n - k)]
        for i in range(n):
            matrix[i][j] = rotate[i]
for i in matrix:
    print(' '.join(i))
