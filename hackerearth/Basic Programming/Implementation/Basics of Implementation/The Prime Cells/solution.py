def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x ** .5) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))
count = 0
for i in range(n):
    for j in range(n):
        top = grid[i - 1][j] if i > 0 else 0
        left = grid[i][j - 1] if j > 0 else 0
        right = grid[i][j + 1] if j < n - 1 else 0
        bottom = grid[i + 1][j] if i < n - 1 else 0
        if is_prime(top + left + right + bottom):
            count += 1
print(count)
