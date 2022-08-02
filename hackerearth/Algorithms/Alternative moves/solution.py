t = int(input())
for _ in range(t):
    n, a, b = map(int, input().strip().split())
    print(1 if a >= n else 2 * ((n - b - 1) // (a - b)) + 1 if a > b else -1)
