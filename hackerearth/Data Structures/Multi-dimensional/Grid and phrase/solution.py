n, m = map(int, input().strip().split())
grid = []
for _ in range(n):
    grid.append(input().strip())
if n < 4 and m < 4:
    print(0)
else:
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 's':
                if i <= n - 4 and grid[i + 1][j] == 'a' and grid[i + 2][j] == 'b' and grid[i + 3][j] == 'a':
                    count += 1
                if j <= m - 4 and grid[i][j + 1] == 'a' and grid[i][j + 2] == 'b' and grid[i][j + 3] == 'a':
                    count += 1
                if i <= n - 4 and j <= m - 4 and grid[i + 1][j + 1] == 'a' and grid[i + 2][j + 2] == 'b' and \
                        grid[i + 3][j + 3] == 'a':
                    count += 1
                if i >= 3 and j <= m - 4 and grid[i - 1][j + 1] == 'a' and grid[i - 2][j + 2] == 'b' and \
                        grid[i - 3][j + 3] == 'a':
                    count += 1
    print(count)
