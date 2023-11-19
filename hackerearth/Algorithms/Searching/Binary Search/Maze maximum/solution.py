n, m = map(int, input().strip().split())
matrix = []
min_rows = []
for i in range(n):
    matrix.extend(list(map(int, input().strip().split())))
    min_rows.append(min(matrix[i * m :]))
min_cols = []
for i in range(m):
    min_cols.append(min(matrix[i::m]))
print(min(max(min_rows), max(min_cols)))
