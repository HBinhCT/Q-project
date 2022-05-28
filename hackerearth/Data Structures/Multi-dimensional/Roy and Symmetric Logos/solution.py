t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [input().strip() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[-(i + 1)][j] or matrix[i][j] != matrix[i][-(j + 1)]:
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')
