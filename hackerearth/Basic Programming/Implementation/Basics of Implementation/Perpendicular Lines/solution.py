t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().strip().split())
    x3, y3, x4, y4 = map(int, input().strip().split())
    if (x1, y1) == (x2, y2) or (x3, y3) == (x4, y4):
        print('INVALID')
    else:
        a = x2 - x1
        b = y2 - y1
        c = x4 - x3
        d = y4 - y3
        if a * c + b * d == 0:
            print('YES')
        else:
            print('NO')
