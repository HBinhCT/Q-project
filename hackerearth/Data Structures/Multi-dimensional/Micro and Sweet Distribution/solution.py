from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().strip().split())
    sx, sy = map(int, stdin.readline().strip().split())
    dx, dy = map(int, stdin.readline().strip().split())
    ox = n + 1 - sx
    oy = m + 1 - sy if n % 2 else sy
    if ox == dx and oy == dy:
        print('Over')
    elif (not (dx - sx) % 2 and dy == m + 1 - sy) or ((dx - sx) % 2 and dy == sy):
        print('Back' if sx == 1 else 'Front')
    elif not (dx - sx) % 2:
        print('Right' if sy == 1 else 'Left')
    else:
        print('Right' if sy == m else 'Left')
