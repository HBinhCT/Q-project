t = int(input())
for _ in range(t):
    n, m, d = map(int, input().strip().split())
    locations = []
    for _ in range(n):
        locations.append(tuple(map(int, input().strip().split())))
    targets = []
    for _ in range(m):
        targets.append(tuple(map(int, input().strip().split())))
    kill = 0
    for x1, y1 in targets:
        for x2, y2 in locations:
            if abs(x2 - x1) + abs(y2 - y1) <= d:
                kill += 1
                break
    print("YES" if kill > m // 2 else "NO")
