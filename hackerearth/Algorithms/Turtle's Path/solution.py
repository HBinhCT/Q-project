n, m = map(int, input().strip().split())
table = []
result = []
for _ in range(n):
    table.append(list(map(int, input().strip().split())))
    result.append([0] * m)
if n == 1 and m == 1:
    print(1)
    print(1, 1)
else:
    size = 100001
    primes = [True] * size
    primes[0] = primes[1] = False
    i = 2
    while i * i < size:
        if primes[i]:
            for j in range(i * i, size, i):
                primes[j] = False
        i += 1
    if primes[table[n - 1][m - 1]]:
        mod = 1000000007
        moves = ((1, 1), (1, 0), (0, 1))
        result[n - 1][m - 1] = 1
        for x in range(n - 2, -1, -1):
            if primes[table[x + 1][m - 1]]:
                result[x][m - 1] = 1
            else:
                break
        for y in range(m - 2, -1, -1):
            if primes[table[n - 1][y + 1]]:
                result[n - 1][y] = 1
            else:
                break
        for x in range(n - 2, -1, -1):
            for y in range(m - 2, -1, -1):
                for dx, dy in moves:
                    if primes[table[x + dx][y + dy]]:
                        result[x][y] += result[x + dx][y + dy]
                        result[x][y] %= mod
        print(result[0][0])
        if result[0][0] != 0:
            x = y = 0
            print(x + 1, y + 1)
            while x < n - 1 and y < m - 1:
                for dx, dy in moves:
                    if primes[table[x + dx][y + dy]] and result[x + dx][y + dy] > 0:
                        x += dx
                        y += dy
                        print(x + 1, y + 1)
                        break
            if x != n - 1:
                for z in range(x + 1, n):
                    print(z + 1, y + 1)
            elif y != m - 1:
                for z in range(y + 1, m):
                    print(x + 1, z + 1)
    else:
        print(0)
