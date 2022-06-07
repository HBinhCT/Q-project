def cells_sol(N, K, task):
    # Write your code here
    rows = set(range(1, N + 1))
    cols = set(range(1, N + 1))
    result = []
    for i, j in task:
        rows.discard(i)
        cols.discard(j)
        result.append(len(rows) * len(cols))
    return result


N, K = map(int, input().split())
task = []
for _ in range(K):
    i, j = map(int, input().split())
    X = i, j
    task.append(X)

out_ = cells_sol(N, K, task)
for elements in out_:
    print(elements, end=' ')
print()
