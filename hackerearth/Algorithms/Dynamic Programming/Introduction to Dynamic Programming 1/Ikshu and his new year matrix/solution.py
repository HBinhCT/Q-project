from math import inf

size = 10001
n, k = map(int, input().strip().split())
matrix = [tuple(map(int, input().strip().split())) for _ in range(n)]
primes = [2]
sieve = [True] * size
for i in range(3, int(size ** .5) + 1, 2):
    if sieve[i]:
        sieve[i * i::2 * i] = [False] * ((size - i * i - 1) // (2 * i) + 1)
primes += [i for i in range(3, size, 2) if sieve[i]]
operations = [inf] * size
for i in range(size - 1, -1, -1):
    if primes and i == primes[-1]:
        operations[i] = 0
        primes.pop()
    elif i + k < size and operations[i + k] != inf:
        operations[i] = operations[i + k] + 1
minimum = inf
center = None
for i in range(n - 2):
    for j in range(n - 2):
        if inf == operations[matrix[i][j]]:
            continue
        if inf == operations[matrix[i + 1][j + 1]]:
            continue
        if inf == operations[matrix[i + 2][j + 2]]:
            continue
        if inf == operations[matrix[i + 2][j]]:
            continue
        if inf == operations[matrix[i][j + 2]]:
            continue
        cnt = operations[matrix[i][j]]
        cnt += operations[matrix[i + 1][j + 1]]
        cnt += operations[matrix[i + 2][j + 2]]
        cnt += operations[matrix[i + 2][j]]
        cnt += operations[matrix[i][j + 2]]
        if cnt < minimum:
            minimum = cnt
            center = (i + 2, j + 2)
if minimum == inf:
    print('no')
else:
    print('yes')
    print(minimum)
    print(*center)
