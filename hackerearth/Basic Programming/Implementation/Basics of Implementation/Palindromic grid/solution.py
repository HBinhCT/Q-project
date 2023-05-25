from string import ascii_lowercase

t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    g = ''
    for _ in range(n):
        g += input()
    count1 = count2 = 0
    for c in ascii_lowercase:
        cnt = g.count(c)
        if not cnt:
            continue
        elif cnt % 4 and not cnt % 2:
            count2 += 1
        elif cnt % 2:
            count1 += 1
    qy, ry = divmod(n, 2)
    qx, rx = divmod(m, 2)
    if ry and rx and (count1 > 1 or count2 > qy + qx):
        print('NO')
    elif ry and not rx and (count1 > 1 or count2 > qx):
        print('NO')
    elif not ry and rx and (count1 > 1 or count2 > qy):
        print('NO')
    elif not ry and not rx and (count1 > 0 or count2 > 0):
        print('NO')
    else:
        print('YES')
