from sys import stdin

tc = int(stdin.readline())
for _ in range(tc):
    n, m = map(int, stdin.readline().strip().split())
    is_possible = True
    for _ in range(m):
        x, y = map(int, stdin.readline().strip().split())
        if is_possible and (x == y or (x > n and x > y and x > n + y)):
            is_possible = False
    print('YES' if is_possible else 'NO')
