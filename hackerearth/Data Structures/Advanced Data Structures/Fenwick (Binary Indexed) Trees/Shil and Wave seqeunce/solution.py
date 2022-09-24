mx = 100000
mod = 1000000007


def flat_update(array, index, value):
    while index <= mx:
        array[index] += value
        array[index] %= mod
        index += index & -index


def flat_query(array, index):
    total = 0
    while index:
        total += array[index]
        total %= mod
        index -= index & -index
    return total


def matrix_update(array, row, col, value):
    while row <= mx:
        array[row][col] += value
        array[row][col] %= mod
        row += row & -row


def matrix_query(array, row, col):
    total = 0
    while row:
        total += array[row][col]
        total %= mod
        row -= row & -row
    return total


n = int(input())
a = list(map(int, input().strip().split()))
adj = [[0, 0] for _ in range(mx + 1)]
tree = [0 for _ in range(mx + 1)]
ans = 0
for i in a:
    flat_left = flat_query(tree, i - 1)
    flat_right = flat_query(tree, mx) - flat_query(tree, i)
    flat_update(tree, i, 1)
    matrix_left = matrix_query(adj, i - 1, 1)
    matrix_right = matrix_query(adj, mx, 0) - matrix_query(adj, i, 0)
    matrix_update(adj, i, 1, matrix_right + flat_right)
    matrix_update(adj, i, 0, matrix_left + flat_left)
    ans += matrix_left + matrix_right + flat_left + flat_right
    ans %= mod
print(ans)
