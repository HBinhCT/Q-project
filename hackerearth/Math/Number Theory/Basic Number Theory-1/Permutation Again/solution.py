from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(1 if n == 1 else n * n // 2 - 1)
