import numpy as np

n, m = map(int, input().strip().split())
mask_size = 2 * m + 1
f = np.empty((mask_size, mask_size))
for i in range(mask_size):
    f[i] = np.array(list(map(int, input().strip().split())))
g = np.empty((n, n))
for i in range(n):
    g[i] = np.array(list(map(int, input().strip().split())))
ops_size = n + 2 * m
ops = np.zeros((ops_size, ops_size))
ops[m:-m, m:-m] = g
new_g = np.ones((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        op = np.array(ops[i:i + mask_size, j:j + mask_size])
        op *= f
        new_g[i][j] = np.sum(op)
for i in new_g:
    print(*i)
