t = int(input())
for _ in range(t):
    n, a, b, c, d, move = map(int, input().strip().split())
    e = max(abs(c - n), abs(d - b))
    if move:
        e -= 1
    print("Draw" if e <= n - a else "White Wins")
