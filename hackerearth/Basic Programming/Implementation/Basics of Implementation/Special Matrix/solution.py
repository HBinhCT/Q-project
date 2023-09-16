t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [input().strip() for _ in range(n)]
    x = y = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "*":
                x = i
                y = j
                break
        else:
            continue
        break
    m = n // 2
    print(abs(m - x) + abs(m - y))
