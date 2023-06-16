t = int(input())
for _ in range(t):
    x, y, z = map(int, input().strip().split())
    a, b = map(int, input().strip().split())
    y0 = y - a
    y1 = y + a
    z0 = z - b
    z1 = z + b
    points = [max(y0, z0), max(y0, z1), max(y1, z0), max(y1, z1)]
    bets = [0]
    for i in points:
        v = i + 1 - x
        if 0 < v <= x:
            bets.append(v)
    ans = max_count = 0
    for i in bets:
        count = 0
        for j in points:
            if x + i > j:
                count += 1
            if x - i > j:
                count += 1
        if count > max_count:
            max_count = count
            ans = i
    print(ans)
